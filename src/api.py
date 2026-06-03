import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from typing import List, Optional

import feedparser

from src.logger import logger
from src.models import Paper

ARXIV_REQUEST_TIMEOUT_SEC = 120
ARXIV_MAX_RETRIES = 5
ARXIV_RETRY_DELAY_429_SEC = 15
ARXIV_RETRY_DELAY_NETWORK_SEC = 5


class ArxivClient:
    """ArXiv API client"""

    def __init__(
        self,
        max_results: int = 500,
        base_url: str = "http://export.arxiv.org/api/query",
        categories: Optional[List[str]] = None,
    ):
        self.max_results = max_results
        self.base_url = base_url
        self.categories = categories or ["cs.CV", "cs.CL", "cs.AI", "cs.LG", "cs.MM"]

    def fetch_papers(self) -> List[Paper]:
        """Fetch latest papers by querying each category separately and merging."""
        per_cat = max(self.max_results // len(self.categories), 50)
        all_papers: List[Paper] = []
        seen_ids: set = set()

        for i, cat in enumerate(self.categories):
            params = {
                "search_query": f"cat:{cat}",
                "max_results": per_cat,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
            url = self.base_url + "?" + urllib.parse.urlencode(params)
            logger.info(f"Fetching category {cat} ({i + 1}/{len(self.categories)}), up to {per_cat} papers...")

            body = self._fetch_feed_body(url)
            if body is None:
                logger.warning(f"Skipping category {cat} due to fetch failure")
                continue

            feed = feedparser.parse(body)
            if getattr(feed, "bozo", False) and feed.bozo_exception:
                logger.warning(f"ArXiv feed parse warning for {cat}: {feed.bozo_exception}")

            count = 0
            for entry in feed.entries:
                paper = self._parse_entry(entry)
                paper_id = paper.link.strip()
                if paper_id not in seen_ids:
                    seen_ids.add(paper_id)
                    all_papers.append(paper)
                    count += 1

            logger.info(f"  {cat}: got {count} new papers (total unique: {len(all_papers)})")

            if i < len(self.categories) - 1:
                time.sleep(3)

        logger.info(f"Fetched {len(all_papers)} unique papers across {len(self.categories)} categories")
        return all_papers

    def _fetch_feed_body(self, url: str) -> Optional[str]:
        """Fetch ArXiv feed with retry. Returns None on persistent failure."""
        for attempt in range(1, ARXIV_MAX_RETRIES + 1):
            try:
                with urllib.request.urlopen(url, timeout=ARXIV_REQUEST_TIMEOUT_SEC) as resp:
                    return resp.read().decode("utf-8")
            except urllib.error.HTTPError as e:
                if e.code in (429, 503) and attempt < ARXIV_MAX_RETRIES:
                    sleep_sec = ARXIV_RETRY_DELAY_429_SEC
                    logger.warning(
                        f"ArXiv {e.code} {e.reason}, sleeping {sleep_sec}s "
                        f"before retry {attempt + 1}/{ARXIV_MAX_RETRIES}"
                    )
                    time.sleep(sleep_sec)
                    continue
                logger.error(f"ArXiv HTTP error: {e.code} {e.reason}")
                return None
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                if attempt < ARXIV_MAX_RETRIES:
                    logger.warning(
                        f"ArXiv network error: {e}, sleeping "
                        f"{ARXIV_RETRY_DELAY_NETWORK_SEC}s before retry "
                        f"{attempt + 1}/{ARXIV_MAX_RETRIES}"
                    )
                    time.sleep(ARXIV_RETRY_DELAY_NETWORK_SEC)
                    continue
                logger.error(f"ArXiv network error: {e}")
                return None

        logger.error("ArXiv fetch retries exhausted")
        return None

    def _parse_entry(self, entry: dict) -> Paper:
        """Parse paper entry"""
        return Paper(
            title=self._clean_text(entry.get("title", "")),
            authors=[self._clean_text(a.get("name", "")) for a in entry.get("authors", [])],
            abstract=self._clean_text(entry.get("summary", "")),
            link=self._clean_text(entry.get("link", "")),
            tags=[t.get("term", "") for t in entry.get("tags", [])],
            comment=self._clean_text(entry.get("arxiv_comment", "")),
            date=self._parse_date(entry.get("published", "")),
        )

    @staticmethod
    def _clean_text(text: str) -> str:
        return " ".join(text.replace("\n", " ").split())

    @staticmethod
    def _parse_retry_after(retry_after: Optional[str], default: int) -> int:
        try:
            if retry_after is None:
                return default
            parsed = int(retry_after)
            return parsed if parsed > 0 else default
        except (TypeError, ValueError):
            return default

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        try:
            return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except (ValueError, TypeError, OSError) as e:
            logger.warning(f"Failed to parse date {date_str!r}: {e}")
            return datetime.now()

# Daily Papers - 自动化每日精选 arxiv 论文

**自动抓取ArXiv论文，使用 Google Gemini 评分筛选高质量内容**

专为 **计算机科学学者/程序员** 设计

## ✨ 特性

- **🆓 完全免费** - 使用 Google AI Studio 免费 API
- **🤖 自动运行** - GitHub Actions 每天自动运行
- **🎯 智能评分** - 四维度评估（0-100分）
- **💡 AI摘要** - 自动生成论文核心贡献摘要

## 🚀 快速开始

1. **Fork 本仓库**
2. **配置 API Key** - 添加 `GOOGLE_AI_API_KEY` 到 GitHub Secrets（[获取地址](https://aistudio.google.com/apikey)）
3. **启用 Actions** - Actions → Daily Papers → Enable workflow
4. **订阅通知** - Watch → All Activity

完成！系统每天 UTC 17:00（北京时间 1:00）自动运行。

📖 **详细设置请查看 [SETUP.md](SETUP.md)**

## 📚 历史论文

查看所有历史精选论文：[papers](papers/)

---

<!-- PAPERS_START -->

## 2026-07-26

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Assisting Mission-Critical Traffic Flows with Active Queue Management in Industrial Internet of Things](https://arxiv.org/abs/2607.14478v1)** | ⭐ 70/100 | 利用AQM优化IIoT关键流量的延迟与抖动 | 针对工业物联网环境的AQM实践，实验评估详实，具有工程落地价值。 | <details><summary>展开</summary>Mission-critical Industrial Internet of Things (IIoT) traffic flows require bounded network latency and jitter guarantees to ensure the safe functioning of critical industrial infrastructure. These flows are typically communicated via commodity network routers with conventional First-In-First-Out (FIFO) buffers. FIFO has proven to be the culprit of the well-known bufferbloat phenomenon, and the deployment of Active Queue Management (AQM) schemes have demonstrated significant performance improvements for latency-sensitive applications over the Internet in the IT domain. However, the bufferbloat phenomenon and the efficacy of AQM schemes have not been studied in IIoT-based OT domain. In this paper, we propose the use of AQM as a lightweight and non-intrusive mechanism for assisting mission-critical traffic flows in IIoT networks. Our experimental results demonstrated that multi-queue AQM schemes provide substantial flow isolation and capacity sharing benefits, and significantly improve the performance of mission-critical traffic flows under network pressure. We further provide deployment recommendations based on our experimental insights.</details> |


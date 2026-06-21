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

## 2026-06-22

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Understanding the "Airport" Censorship Circumvention Ecosystem in China](https://arxiv.org/abs/2606.18427v1)** | ⭐ 70/100 | 系统性分析中国机场翻墙生态 | 实证研究扎实，但非工程系统实现类论文 | <details><summary>展开</summary>In China, a burgeoning underground market sells citizens subscription-based censorship circumvention proxies known as ''airports''. We present the first systematic study of this ecosystem, combining user surveys, social media analysis, and active network measurements. We find that airports are by far the most popular off-the-shelf censorship circumvention tool in China, used by over half of our 1,667~survey respondents, who cite their ease of use, performance, and access to geo-restricted services like ChatGPT and Netflix. By scanning the Internet and scraping Telegram announcement channels, we identify 3,431 active airports built on a handful of open-source toolkits. We subscribe to 35 airports and characterize their performance, which often surpasses direct connections through the Great Firewall due to a distinctive multi-hop architecture. However, airports also pose new challenges and security risks: they accept payment through commercial services like Alipay, suffer frequent government takedowns, and are difficult for clients to configure optimally. Many airports also deploy their own distinct censorship policies. Airports are far more widely used than other circumvention tools from the academic literature, but introduce new forms of fragility and control, offering both lessons and opportunities for future circumvention research.</details> |


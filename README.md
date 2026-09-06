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

## 2026-09-07

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Mobile Backscatter Communication for the Battery-less Internet of Things](https://arxiv.org/abs/2609.01465v1)** | ⭐ 70/100 | 无源物联网移动反向散射通信优化 | 针对移动场景的通信决策系统，原型评估扎实。 | <details><summary>展开</summary>We enable backscatter communication in the battery-less mobile Internet of Things (IoT). Backscatter communication is extensively studied in static settings. Existing designs are, however, fundamentally mismatched with mobility and time-varying energy patterns. Channel conditions rapidly fluctuate, impacting the achievable data rates and thus transmission costs. Energy availability varies unpredictably, possibly forcing devices to remain quiescent to recharge energy buffers. The two issues compound each other: while recharging, a battery-less mobile IoT device may miss more favorable channel conditions. We design a lightweight decision system that dynamically determines when to transmit by checking short-term trends in signal strength, while using Non-volatile Memory (NVM) to retain packets in unfavorable channel conditions and across energy failures. Using a prototype we built and real-world mobility and power traces, we compare our design against a rate-adaptive baseline that only considers the instantaneous channel conditions. Experimental results show that our system improves throughput by up to 5.16x while reducing transmission energy consumption by up to 47.3%, with only 0.23% - 7.3% additional energy overhead.</details> |


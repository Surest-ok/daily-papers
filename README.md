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

## 2026-08-02

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[DISCO: Distributed Spectrum Compliance and Orchestration for Scalable IoT Coexistence](https://arxiv.org/abs/2607.21387v1)** | ⭐ 74/100 | 提出分布式频谱合规与编排架构 | 架构设计实用，通过UAV实测验证了有效性 | <details><summary>展开</summary>Massive Internet of Things (IoT) deployments increasingly share spectrum with incumbent, licensed, and unlicensed systems under uncertain traffic, fading, mobility, and intermittent coordination. Existing mechanisms, including fixed power limits, listen-before-talk procedures, spectrum access databases, and learning-based resource allocation, address important aspects of coexistence, but they do not provide a common control plane to translate a network-wide interference risk budget into lightweight guidance for many autonomous devices. This article introduces Distributed Spectrum Compliance and Orchestration (DISCO), a hierarchical architecture that separates local spectrum learning from edge-level compliance regulation and slower cloud or non-terrestrial-network context adaptation. DISCO is not presented as a new reinforcement-learning optimizer or as a replacement for statutory spectrum rules. Its contribution is a deployable compliance plane that monitors violation statistics, broadcasts a compact governance signal, and adjusts policy aggressiveness without centralizing every transmission decision. A 30-seed UAV coexistence case study illustrates the efficiency--risk trade-off: the reported mean throughput is 81.0~Mbps, 73\% above fixed-power control, while the mean violation rate is 0.053 compared with 0.126 for uncoordinated learning. Because the 95\% confidence interval, [0.030, 0.076], crosses the nominal target of 0.06, the evidence supports statistical regulation near the target, not guaranteed regulatory compliance. Deployment, complexity, adoption boundaries, and open validation requirements are discussed explicitly.</details> |


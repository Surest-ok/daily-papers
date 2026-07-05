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

## 2026-07-06

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Enabling Real-Time AI in O-RAN: Deploying andMeasuring AI Inside a Near-RT RIC xApp](https://arxiv.org/abs/2607.01583v1)** | ⭐ 75/100 | 在O-RAN近实时RIC中实现轻量级AI推理部署 | 通过C语言嵌入式推理满足O-RAN时延约束，工程实现扎实 | <details><summary>展开</summary>Open Radio Access Network (O-RAN) architectures introduce programmable Near-Real-Time RAN Intelligent Controllers (Near-RT RICs) that support closed-loop control through xApps at timescales from 10 ms to 1 s. Although AI has been widely studied for RAN optimization, fewer works demonstrate measured AI inference embedded directly within the Near-RT RIC software loop on a live testbed. This paper presents an AI-enabled network-state classification xApp implemented on an OpenAirInterface (OAI) and FlexRIC testbed. The xApp is trained and evaluated on a structured synthetic dataset that emulates cross-layer RAN states using MAC, RLC, PDCP, GTP, and UE-count features. The results validate embedding and execution feasibility rather than production-level generalization. Logistic regression and a shallow multilayer perceptron (MLP) are exported as deterministic C inference modules and compiled into the xApp binary, eliminating external machine-learning runtime dependencies. Measured inference latency is 1 to 5 microseconds for logistic regression and 10 to 25 microseconds for the MLP, while end-to-end service latency remains below 4 ms. A six-model comparison shows that supervised models achieve similar accuracy, ranging from 0.88 to 0.90, indicating that LR and MLP similarity reflects the proxy problem structure rather than limited model exploration. Noise ablation, confusion-matrix analysis, and CDF-based latency characterization show that both embedded models satisfy the 10 ms Near-RT budget for more than 95% of projected loop executions. These results demonstrate that lightweight AI can operate within Near-RT RIC timing constraints while preserving deterministic execution. We also release RIC Workbench, a lightweight orchestration dashboard for reproducing the testbed on commodity hardware.</details> |


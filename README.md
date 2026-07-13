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

## 2026-07-14

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Hybrid Quantum and Classical Workload Management with Graph-based Scheduling](https://arxiv.org/abs/2607.09151v1)** | ⭐ 82/100 | 基于Kubernetes的量子-经典混合负载调度器 | 针对混合计算的调度优化，具备真实硬件评估与工程价值。 | <details><summary>展开</summary>High Performance Computing (HPC) centers are expanding to encompass resources that extend beyond traditional computing. By extending resources to quantum computing, hybrid quantum-classical workflows tackle complex optimization problems that have never before been possible. However, integrating quantum processing units (QPUs) into cloud-native and scientific workload managers presents a unique orchestration challenge: remote quantum devices introduce a second, external queue -- a two-queue problem -- alongside the queue owned by the traditional scheduler. In this work we present Fluence, a Kubernetes scheduler plugin backed by the Fluxion graph-based scheduler, that enables informed, gang-scheduled placement for quantum-classical workloads and custom resources. We evaluate Fluence across three scenarios using AWS Braket simulators and real QPUs. First, under node contention, Fluence's atomic gang placement all but eliminates the wasted node-time that a default scheduler accrues by partially placing gangs. Second, we introduce a synchronization primitive for the two-queue problem in which a single producer submits a shared quantum task while consumers remain scheduling-gated, reducing worker idle time by roughly 5x under short device queues and by orders of magnitude when a real device queue stretched to hours. Third, cost- and queue-aware backend selection pins the cheapest or shortest-queue device satisfying a workload, cutting mean per-run cost by roughly 70x and time-to-result from hours to under a minute. Together, these results show that quantum-awareness can be added to a cloud-native scheduler without modifying user containers.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Privacy-Preserving Intent Fulfilment and Assurance for 6G RAN](https://arxiv.org/abs/2607.08809v1)** | ⭐ 78/100 | 6G RAN隐私保护意图管理架构 | 架构设计严谨，利用生产数据验证，符合工程实践。 | <details><summary>展开</summary>Intent-based network management is the emerging paradigm for 6G service lifecycle automation, with the 3GPP intent management framework (TS~28.312) defining creation, translation, fulfilment, and assurance stages. Existing fulfilment and assurance approaches require deep packet inspection, per-flow state tracking, or access to vendor-internal node telemetry to verify that provisioned resources satisfy expressed intents. These requirements conflict with regulatory constraints (GDPR, ePrivacy Directive) in multi-tenant networks and with vendor opacity in multi-vendor O-RAN deployments. We present an architecture for privacy-preserving intent fulfilment and assurance in which a coordinator provisions resources from declared intent categories without traffic inspection, and verifies fulfilment using only aggregate standardised PM counters at the O1 interface. A data-processing inequality argument shows that the resource allocation reveals at most $\log_2 K$ bits about traffic content, where $K$ is the number of intent categories. We define two architectural privacy properties, intent-traffic unlinkability and node-opaque verification, and show that both hold by construction. Node-opacity does not sacrifice detection power: the aggregate verifier weakly dominates the per-agent verifier under a homogeneity condition. We map the architecture to the 3GPP intent lifecycle and the O-RAN Non-RT RIC, identifying the concrete interfaces, data objects, and deployment points at which the mechanism operates. On production PM counter data from four operator networks, increasing intent-category granularity sharpens provisioning but weakens assurance, consistent with the theoretical prediction that the privacy ceiling is a structural side effect of the detection constraint rather than a separate design parameter.</details> |


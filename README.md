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

## 2026-10-04

## OS Kernel & Scheduling

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Vulnerability-Weighted Routing of Timing-Critical Nets for Configuration-Upset-Resilient SRAM-Based FPGAs](https://arxiv.org/abs/2610.00281v1)** | ⭐ 78/100 | 提出一种FPGA布线抗干扰优化方法 | 针对FPGA硬件可靠性的工程优化，实验扎实且具备实用价值 | <details><summary>展开</summary>Conventional FPGA routing optimizes timing, congestion, and routability but does not distinguish routes with similar nominal performance and substantially different susceptibility to configuration-induced delay degradation. This paper presents a vulnerability-weighted routing methodology for SRAM-based field-programmable gate arrays (FPGAs) that incorporates predicted routing-fault severity directly into the routing objective. A continuous vulnerability cost relates delay perturbations caused by electrically attachable dormant routing resources to the available downstream timing slack, while a complementary configuration-concentration term discourages excessive localization of vulnerable resources. To limit implementation disruption, only the highest-risk nets are selectively ripped up and rerouted while unaffected routes remain fixed. The method is implemented on a Zynq UltraScale+ XCZU7EV using a Vivado/RapidWright-based flow and evaluated across four routed benchmarks against commercial timing-driven routing, vulnerability-agnostic rerouting, and binary vulnerable-resource avoidance. Controlled configuration-equivalent perturbations provide hardware-level validation. The proposed method reduces aggregate configuration-induced timing vulnerability by 41.7% with approximately 1.0% nominal timing degradation and captures 85.8% of the vulnerability reduction obtained at the expanded routing budget by rerouting only the highest-risk 5% of eligible nets. The results demonstrate that continuous vulnerability information can improve configuration-upset resilience with limited impact on nominal routing quality.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Analyzing 10 Petabit/s Network Data with Accelerated Associative (Token) Arrays](https://arxiv.org/abs/2609.32978v1)** | ⭐ 75/100 | 利用GPU加速关联数组实现超大规模网络数据分析 | 通过GPU加速实现了高性能网络分析，具备良好的可扩展性与工程实现价值。 | <details><summary>展开</summary>As networks expand and become an ever more critical infrastructure to modern society the need to analyze these networks with the highest regard for privacy is essential to ensure their proper function. Depending on the level of the network layer to be analyzed, sources and destinations can be any combination of physical, logical, or persona/agentic endpoints, which requires the ability to handle diverse data. Invaluable to these analyses are mathematical tools that enable sophisticated mathematical algorithms to be expressed succinctly while achieving scalable vertical (within a compute node), horizontal (across compute nodes), and temporal (over different generations of hardware) performance. Associative (token) array mathematics and corresponding libraries is one approach that can meet these requirements. Accelerating these libraries with GPUs enables the analysis of the largest networks. The MIT/IEEE/Amazon Anonymized Network Sensing Graph Challenge provides a venue for highlighting the applicability of accelerated associative arrays for these types of problems. The D4M associative library has been implemented in a number of languages. This work benchmarks a prototype Matlab D4M GPU accelerated implementation of the Anonymized Network Sensing challenge across a wide range of CPU and GPU hardware. Scalable performance is demonstrated within and across CPU cores, CPU nodes, and GPU nodes. Horizontal scaling across multiple nodes was linear. Running on hundreds of GPU nodes simultaneously achieved a sustained processing rate sufficient to potentially analyze a 10 Petabit/s network.</details> |


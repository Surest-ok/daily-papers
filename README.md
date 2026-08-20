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

## 2026-08-21

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Demo: tfdrift - A Severity Taxonomy and Risk Classification Framework for Infrastructure Drift Detection](https://arxiv.org/abs/2608.18173v1)** | ⭐ 82/100 | 提出tfdrift框架以分级过滤IaC配置漂移告警 | 实用性强，在生产环境验证了告警降噪效果 | <details><summary>展开</summary>Infrastructure as Code (IaC) tools like Terraform have become the standard for declarative cloud resource management, yet configuration drift, where deployed infrastructure diverges from its declared state, remains a persistent operational and security challenge. Current detection approaches treat all changes equivalently, contributing to alert fatigue that causes operators to miss security-critical modifications. We propose a generalized severity taxonomy for infrastructure drift that classifies changes into four risk tiers based on resource type and attribute-level impact. We implement this taxonomy in tfdrift, an open-source classification framework with 60+ configurable rules covering AWS, Azure, and GCP resource patterns (evaluation reported here is AWS-focused). Evaluation across 150+ AWS Terraform workspaces demonstrates that severity filtering reduces alert volume by 73% while retaining 94% of security-relevant changes, offering a lightweight alternative to ML-based alert filtering. tfdrift is available at github.com/sudarshan8417/tfdrift.</details> |
| **[Reproducibility is Not Enough: Artifact Verifiability in Decentralized-Build Package Ecosystems](https://arxiv.org/abs/2608.18180v1)** | ⭐ 78/100 | 构建自动化流水线评估去中心化包生态的可验证性 | 通过实证研究揭示了供应链安全中元数据缺失的痛点 | <details><summary>展开</summary>Reproducible and verifiable builds increase trust in distributed software artifacts by enabling independent parties to detect artifacts produced by compromised build or release pipelines. However, artifact verification requires more than deterministic builds: a verifier must also recover the source state, build environment, dependencies, and build instructions that produced the artifact. Decentralized-build ecosystems make this difficult because artifacts are produced through heterogeneous tools, maintainer-controlled workflows, and fragmented metadata. As a result, it remains unclear how often artifacts in these ecosystems can be independently verified. This paper studies artifact verifiability across four popular decentralized-build package ecosystems. We define an independent verifier model that relies only on registry-derivable metadata and an artifact comparison model with tiered equivalence levels. We implement these models in an Artifact Verification Pipeline and use it to measure artifact verifiability across the target ecosystems. Our results show that, beyond build determinism, verifiability is limited by missing source and build metadata, implicit release transformations, and unconventional build practices. Provenance attestations and embedded VCS metadata improve verification, but they do not provide complete rebuild specifications. These findings identify concrete metadata gaps and ecosystem-level changes needed to make artifact verification practical at package-registry scale.</details> |
| **[When Do Microservices Save Energy? Evidence from Environmental Simulation Workflows](https://arxiv.org/abs/2608.18376v1)** | ⭐ 75/100 | 评估微服务架构对环境模拟工作流的能耗影响 | 通过实测对比单体与微服务架构的能耗，具有工程参考价值 | <details><summary>展开</summary>Environmental simulation models support scenario analysis, calibration, and decision-making, but repeated execution can incur significant energy costs. Microservices offer modularity and scalability, yet their low-carbon impact remains unclear because decomposition introduces orchestration, communication, persistence, and idle-service overheads. This paper evaluates four environmental models as containerised microservice workflows, comparing monolithic execution with polling-based and event-driven orchestration. Results show that microservices increase energy consumption for smaller or tightly coupled models, where coordination overhead dominates. For a larger workflow, event-driven orchestration reduces energy use despite longer runtime, while selective downstream re-execution achieves a 41% reduction during repeated parameter exploration.</details> |

## eBPF & Observability

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[XNET: Intelligent Dynamic Sampling for High-Speed Network Security Monitoring](https://arxiv.org/abs/2608.18349v1)** | ⭐ 88/100 | 基于XDP的动态流量采样与安全监控系统 | 利用XDP实现线速流量处理，具备真实部署验证与高实用性。 | <details><summary>展开</summary>Growing network speeds, with 100GbE line rates becoming common in modern enterprise networks, pose challenges to operators and security applications, as they struggle to scale their operational efficiency accordingly, without relying on costly hardware, excessive sampling, or complex distributed deployments. Unintentional loss due to stochastic packet sampling often produces low-quality traffic, further risking missed detection of critical security incidents, particularly those hidden in typically low-rate traffic, such as APT/malware command-and-control communications. In this paper, we introduce XNET, a system that monitors traffic at line rate using commodity hardware and applies dynamic sampling to amplify the visibility of high security value traffic. XNET leverages Linux's XDP technology to process packets efficiently, classify them based on their security value, and sample them as per configured policies. The outcome is a reduced packet stream in which the security-relevant portion of the traffic is amplified at the expense of less interesting traffic segments. XNET is a highly flexible, scalable and dynamic system that can be adapted based on a network's needs. We deployed XNET in a large real-world network using only commodity hardware, where our results show that XNET can achieve up to 84% traffic reduction with no packet loss while increasing the visibility of otherwise negligible traffic fivefold. With controlled stress tests, we further demonstrate XNET's scalability up to 100Gbps. Additionally, we show that XNET sampling led to a detection rate of 99.6% in an IDS application.</details> |


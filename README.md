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

## 2026-08-25

## OS Kernel & Scheduling

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[MEMPOWER: Efficient Power Management with Fine-grained Memory Analysis and Modeling for HPC Workloads](https://arxiv.org/abs/2608.20734v1)** | ⭐ 75/100 | 基于内存行为分析的HPC功耗管理框架 | 通过细粒度内存分析优化HPC功耗，实验详实且实用。 | <details><summary>展开</summary>Managing the energy consumption and power efficiency of parallel applications is a significant issue in both HPC environments and in the cloud. As emerging applications continue to push against the memory wall of modern machines, the growing imbalance between compute and data movement creates new opportunities to intelligently tune CPU power consumption. Unfortunately, existing frequency and voltage scaling techniques do not adequately capture fine-grained changes in memory access behavior, rendering the compute/data access imbalance invisible to the components of the system that could capitalize on it, thus leaving potential power savings on the table. In this paper, we propose MEMPOWER, a flexible, model-based approach to exposing compute/data movement imbalance that characterizes the fine-grained memory behavior of parallel workloads. This characterization then informs our automated software framework which can statically instrument the application binary with model-determined voltage/frequency transitions that balance fine-grained changes in memory access behavior with the costs of hardware transitions. Using MEMPOWER, we demonstrate a reduction in EDP of 6% to 42% on a range of HPC benchmarks with minimal impact on execution time when compared to the standard OS/hardware-managed power control mechanism.</details> |

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Making Deployments Safe at Meta: Health Checks for Continuous Change-Safety](https://arxiv.org/abs/2608.20513v1)** | ⭐ 88/100 | Meta大规模部署健康检查系统实践 | 工业界大规模生产环境部署保障的宝贵经验 | <details><summary>展开</summary>Continuous deployment to large scale production systems creates a tension between release velocity and reliability. Every change is a potential reliability incident, yet every delay is a missed opportunity. This paper describes the deployment time health check infrastructure that Meta uses to mediate this tension across thousands of heterogeneous services. We summarize the architecture of this prevention based distributed system's service called Service Health Checker, explain how check authors compose templated metric queries, thresholds, and workflow predicates; and discuss how the system is integrated with tiered and phased rollouts so that regressions trigger automatic rollback. We then describe the operational problems that emerged at scale, such as noise, alert fatigue, drift, and uncovered regressions, and the program of measurement, tooling, and improved defaults we deployed to address them. We close with lessons learned from years of operating deployment health checks at Meta, and the directions we are exploring next, including AI assisted health check tuning. Index Terms: deployment safety, continuous deployment, monitoring, software reliability, release engineering, software reliability engineering, AIOps, anomaly detection</details> |
| **[PRICE: Pricing-based Resource Incentives for Quality-of-Result-aware Computing at the Edge](https://arxiv.org/abs/2608.20819v1)** | ⭐ 78/100 | 基于定价机制的边缘计算资源调度与质量权衡方案 | 通过定价调节边缘负载，实测数据充分且具有工程落地价值 | <details><summary>展开</summary>Edge nodes are capacity-constrained by design, yet many edge workloads can trade result quality for resource efficiency at runtime. Existing edge pricing mechanisms largely treat requests as fixed-configuration submissions and rarely exploit per-request quality flexibility under overload. We present PRICE, an incentive mechanism that couples a utilization-dependent price signal to per-request quality selection. As utilization increases, rising acceptance prices make resource-intensive variants less likely to be selected, shifting accepted requests toward lighter execution and allowing the node to serve significantly more requests while operating near capacity. Evaluation on real hardware under sustained overload shows that PRICE outperforms both fixed-allocation and dynamic-pricing baselines in accepted throughput and CPU utilization. The results are robust across pricing function families, task-duration distributions, and client populations. Result-quality flexibility is a powerful but underused control dimension for overload management at the edge, and pricing is an effective mechanism to exploit it.</details> |
| **[Orchra: Stateful-aware Cross-slice Workload Migrations in the 6G Control Plane](https://arxiv.org/abs/2608.20893v1)** | ⭐ 78/100 | Orchra实现5G切片间状态迁移以降低延迟 | 通过外部化状态实现切片迁移，实验数据详实且具工程价值 | <details><summary>展开</summary>Network slicing is a foundational capability of Fifth Generation (5G)-Advanced and emerging Sixth Generation (6G) networks, yet practical support for seamless runtime slice transitions remains limited. Standard cloud-native 5G architectures lack native support for stateful inter/intra-slice session migration, relying instead on high-overhead Non-Access Stratum (NAS) re-registrations, container redeployment etc., which disrupt userplane traffic for up to 245.50 ms. To address this limitation, we present Orchra, an intelligent orchestrator for stateful, low-latency context transfer. By externalizing critical user equipment state-including NAS context, security keys, and Protocol Data Unit (PDU) session information-into a transient staging layer, Orchra preserves session continuity across slice boundaries without requiring full re-registration. Experimental evaluation shows that Orchra reduces this userplane interruption by more than twice in comparison to conventional Third Generation Partnership Project (3GPP)-based approaches while incurring negligible security overhead. These results demonstrate a practical and reproducible approach for enabling seamless, state-preserving slice transitions in cloud-native 5G-Advanced networks.</details> |
| **[Scalable Distributed Simulation-Based Testing for Automated Driving Systems](https://arxiv.org/abs/2608.20904v1)** | ⭐ 78/100 | 基于K8s的自动驾驶仿真测试流水线框架 | 工程实现完整，利用K8s与Argo实现分布式仿真测试，实用性强。 | <details><summary>展开</summary>Virtual scenario-based testing is a key enabler for validating automated driving systems (ADS) and intelligent transport systems (ITS). However, executing large-scale test suites involving possibly thousands of scenarios remains labor-intensive and difficult to scale. This paper presents an end-to-end, DevOps-driven framework that automates build, deployment, and distributed execution of CARLA-based scenario tests of an ADS on a lightweight Kubernetes cluster. ROS 2 applications are packaged as standardized Kubernetes Helm charts generated from repository specifications, while entire simulation environments are composed declaratively via dynamic Helmfile manifests. The paper describes how a distributed testing workflow can be implemented in Argo Workflows to provision environments, aggregate and batch OpenSCENARIO test cases from configurable sources, execute scenarios in parallel across cluster nodes, and collect logs and resource metrics. In an evaluation on a multi-node K3s cluster running 200 scenarios, the best configuration speeds up end-to-end workflow time by more than a factor of eight compared to a sequential baseline. The results demonstrate significant gains in end-to-end execution time and quantify trade-offs between parallelism, orchestration overhead, and cluster stability. The framework is further demonstrated in a real-world ADS test application with connections to scenario sources and downstream evaluation modules. This demonstrates that the approach provides a strong foundation not only for scalable simulation testing, but also for generating traceable evidence that can support safety arguments.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Integrating a Python Dynamical core into ICON](https://arxiv.org/abs/2608.21150v1)** | ⭐ 78/100 | 利用Python与DaCe优化气候模型核心性能 | 通过DSL实现高性能计算代码生成，具备实际部署价值 | <details><summary>展开</summary>The transition of Earth-system models to exascale is often hindered by rigid, monolithic Fortran codebases and maintenance-heavy compiler directives. While high-level DSLs offer a solution, they frequently fail due to cumbersome integration. We present the integration of a Python-based ICON dynamical core into the original Fortran simulation code. Leveraging the GT4Py DSL and the Data-Centric (DaCe) optimization framework, we demonstrate that high-level Python can be seamlessly integrated into legacy infrastructure without performance loss. Our results challenge the assumption that Python orchestration introduces prohibitive HPC overhead. In production-grade global simulations, our Python dynamical core achieves a 20--30\% performance improvement over the highly-optimized Fortran+OpenACC implementation, with a 10\% improvement on the total time for a coupled setup. Driven by advanced data-flow optimizations and automated kernel fusion, this approach replaces hardware-entangled directives by generating optimized device code from a single, portable Python source. This work proves that Python can provide a sustainable, efficient, and hardware-agnostic future for global climate modeling.</details> |


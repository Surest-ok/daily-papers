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

## 2026-06-26

## OS Kernel & Scheduling

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis](https://arxiv.org/abs/2606.25863v1)** | ⭐ 78/100 | 通过静态分析自动识别内核配置漏洞影响范围 | 方法实用且评估规模大，对内核安全维护有直接价值 | <details><summary>展开</summary>We study how security patches in highly configurable C/C++ systems map onto the space of compile-time variants. We formalize the Vulnerability Impact Condition (VIC) - a Boolean predicate over configuration options that denotes all variants that contained the original flaw - and introduce PatchLens, a purely static technique that recovers VICs by aligning AST-level patch hunks with source-level presence conditions and resolving file inclusion via lightweight build system analysis. Evaluating PatchLens on 1,192 Linux kernel, 289 FFmpeg, and 100 PHP patches, we compute precise, human-readable VICs without the need to compile any system variant. The resulting predicates are compact (avg. 1.84 variables for Linux, 3.23 for FFmpeg, 1.04 for PHP) and show that only a small fraction of vulnerabilities are system-wide, which carry higher CVSS scores; meanwhile, CVE texts almost never encode the required options ($\approx$ 1% average recall), motivating automated enrichment of CVE descriptions with VICs. PatchLens and the accompanying dataset enable immediate applications in CI (variant-aware triage and test selection), targeted sampling and fuzzing, and feature risk scoring, offering a scalable, explainable path to vulnerability assessment in highly configurable software.</details> |

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Dependency-Aware Dominant Resource Fairness for Multi-Tenant Multi-Resource Systems](https://arxiv.org/abs/2606.25540v1)** | ⭐ 78/100 | 提出DDRF调度策略以优化多租户资源分配效率 | 针对多资源依赖的调度优化，评估详实且具实用价值 | <details><summary>展开</summary>Multi-resource allocation in network-congested, multi-tenant systems in which demand exceeds available capacity is challenging, as there is no straightforward way to determine how much of each resource to assign, especially when resources are interdependent. Classical approaches such as Dominant Resource Fairness (DRF), which generalizes Max-Min Fairness (MMF) to multiple resources, assume linear proportional dependencies across resources, requiring allocations to follow fixed proportions implied by tenants demands. However, this assumption may lead to inefficient allocations and resource waste, with allocated resources that go unused in practice. In this paper, we consider a multi-resource orchestrator and propose the Dependency-aware Dominant Resource Fairness (DDRF) policy, a centralized generalization of DRF that considers inter-resource dependencies: it equalizes active dominant shares of congested resources, preserving DRFs desirable properties, while avoiding its inefficiency with low-demand tenants. We prove that DDRF always saturates at least one congested resource, ensuring Pareto efficiency and eliminating resource waste. We evaluate DDRF using Amazon EC2 traces and a virtualized radio access network (vRAN) use case while considering real resource dependencies. The results show that DDRF improves effective user satisfaction by up to 80% and reduces resource waste by up to 60% compared to dependency-agnostic baselines, while improving Jain's fairness index by more than 15% compared to the utilitarian policy.</details> |

## eBPF & Observability

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[ActPlane: Programmable OS-Level Policy Enforcement for Agent Harnesses](https://arxiv.org/abs/2606.25189v1)** | ⭐ 78/100 | 基于eBPF的AI代理OS级策略执行引擎 | 利用eBPF实现内核级策略强制执行，具备实用性与开源实现 | <details><summary>展开</summary>AI agents increasingly run in production through harnesses, the software around the LLM, including an engine that enforces safety and effectiveness policies, e.g., 'run tests before committing.' Enforcing these policies requires bridging a semantic gap: policy intent is expressed in underspecified natural language, while enforcement must act on concrete system actions, e.g., which test to run. Many policies also define event ordering or data flow actions. Yet existing approaches fall short. Tool-call guardrails miss system actions that bypass the tool layer, while OS sandboxes control resource access instead of actions, returning opaque errors that confuse the agent. Our key insight is that policy context lives within the agent closest to the task, while enforcement must happen at the OS to cover all execution paths. We introduce ActPlane, a policy engine that lets agents declare policies and enforces them in the OS kernel with semantic feedback and isolation. ActPlane uses a simple information-flow control (IFC) DSL to support cross-event policies. We implement ActPlane with eBPF and evaluate it on policies from the empirical study, coding-task benchmarks, and safety benchmarks. ActPlane improves policy compliance, including on indirect execution paths that tool-call interception cannot observe, with 1.9%-8.4% overhead. ActPlane is at https://github.com/eunomia-bpf/ActPlane</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Endeavor: Efficient PairHMM for Detection of DNA Variants in Genome-Scale Datasets](https://arxiv.org/abs/2606.25738v1)** | ⭐ 75/100 | 提出高效PairHMM并行策略加速基因变异检测 | 针对生物信息学瓶颈的算法优化，实测性能提升显著 | <details><summary>展开</summary>DNA variant calling represents a key operation in bioinformatics pipelines that aims at identifying genetic variants. Given an evidenced explosion in genomic data availability, there is an urgent need for a high-performant, portable and efficient solution for variant calling, which can further improve our understanding of genomic structure and genetic basis for complex diseases. In its most common formulation, the Pair Hidden Markov Model (PairHMM) algorithm for variant calling stands as the main bottleneck in the pipeline, accounting for up to 70% of the execution time in large-scale genomic datasets. The state-of-the-art approaches for accelerating PairHMM in CPUs and GPUs do not scale to long DNA sequences and only explore very limited anti-diagonal data parallelism, which yields poor performance. In this work, Endeavor is proposed as a new parallelization strategy for PairHMM that redefines its traditional formulation to explore row-level fine-grained parallelism without loss in solution accuracy. Based on this, a novel and portable SIMD-based approach is derived for efficient and high-performance processing of short and long sequences in CPUs and GPUs, leveraging novel levels of parallelism and synchronization to achieve high throughput in sequences up to 100k basepairs for the first time. Evaluation on Intel and AMD CPUs shows that Endeavor outperforms GKL up to 2.14x in peak throughput and GATK HaplotypeCaller by at least 2x in real-world datasets, while NVIDIA and AMD GPUs achieve up to 2.05x speedups in genome-scale datasets when compared to state-of-the-art GPU-based methods.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Ambulance: saving BFT through racing](https://arxiv.org/abs/2606.25099v1)** | ⭐ 82/100 | 通过协议竞争机制优化BFT共识的延迟与吞吐量 | 提出创新的竞争式BFT协议，实验严谨且具备实用价值 | <details><summary>展开</summary>Today's practical Byzantine Fault Tolerant (BFT) state machine replication deployments are vulnerable to slowdowns. The main culprit is timeouts. Aggressive timeouts spuriously trigger expensive leader changes, while conservative timeouts leave the system idle and let slowdowns severely inflate latency. Two main alternatives exist: hedging, which improves recovery from slow leaders but still incurs a time-based hedging delay, and cooperative asynchronous protocols, which recover quickly from slowdowns but suffer from high common-case latency and low throughput. This paper presents Ambulance: a BFT state machine replication protocol that sidesteps this trade-off through protocol-rigged races, where replicas, rather than race against the clock, race against each other by executing protocol steps. This enables Ambulance to achieve high throughput and low latency comparable to state-of-the-art timeout-based BFT, while matching the robustness of cooperative approaches.</details> |


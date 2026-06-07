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

## 2026-06-08

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving](https://arxiv.org/abs/2605.03375v1)** | ⭐ 75/100 | Tutti：面向长上下文LLM推理的SSD KV缓存方案 | 新颖的GPU存储栈和IO调度，解决了SSD KV缓存性能瓶颈，有实际系统实现和评估，但核心是LLM服务优化，非纯系统研究。 | <details><summary>展开</summary>LLM serving relies on prefix caching to improve inference performance. As growing contexts push key-value (KV) cache footprint far beyond GPU HBM and CPU DRAM capacity, KV cache is increasingly offloaded to NVMe SSDs. Unfortunately, restoring KV cache from SSDs suffers from poor I/O performance and incurs significant GPU stalls. This is primarily because the fragmented GPU memory layout results in a massive number of tiny random I/Os, rendering the low-parallelism CPU a severe bottleneck even with GPU Direct Storage (GDS), which still relies on CPU intervention to initiate each I/O and thus remains CPU-centric. This paper presents Tutti, an efficient SSD-backed KV caching solution that eliminates CPU intervention from the critical data and I/O control paths between HBM and SSDs. At the core of Tutti is a GPU-centric KV cache object store, in which the CPU is only responsible for asynchronously loading I/O kernels once per layer to the GPU. Tutti saturates NVMe SSD bandwidth and reduces GPU stalls to near zero through the following designs: (i) we provide a GPU-native object abstraction that enables bulk KV cache transfers and management; (ii) we re-architect the GPU storage stack by introducing GPU io_uring to support asynchronous GPU direct object I/O; and (iii) we propose slack-aware I/O scheduling to avoid GPU resource contention. We have implemented Tutti and integrated it to vLLM. Extensive evaluation shows that compared to the state-of-the-art GDS-enabled, SSD-backed LMCache, Tutti reduces TTFT by 78.3% under strict SLO constraints and improves the achievable request rate by 2x. The serving cost is reduced by 27%. Tutti achieves nearly the same inference performance as DRAM-backed LMCache, while providing almost infinite capacity.</details> |
| **[Virtual-Memory Powersort](https://arxiv.org/abs/2605.27147v1)** | ⭐ 75/100 | 一种低内存占用的自适应归并排序算法 | 算法优化显著，且有实证评估，实用性较强 | <details><summary>展开</summary>We give a more space-efficient implementation of adaptive mergesort: Virtual-Memory Powersort. Using internal buffering techniques, we significantly reduce the memory consumption of the algorithm; specifically, for sorting $n$ objects the required buffer area is reduced from space for $n/2$ objects to $O(\sqrt{n \log n})$ objects. While this space-efficiency can be achieved (indeed reduced to $O(1)$) conceptually very easily with known inplace merging algorithms, using these as a drop-in replacement for the standard merge algorithm incurs a substantial slow-down. Virtual-Memory Powersort, by contrast, uses the same number of moves and comparisons as previous Powersort implementations up to an additive $O(n)$ term. We report on an empirical running-time study comparing our implementation against other Powersort variants and state-of-the-art stable sorting methods, demonstrating that almost in-place stable sorting can be achieved with negligible overhead in many scenarios.</details> |
| **[A Virtual Processor brings back the Free Lunch](https://arxiv.org/abs/2605.30507v2)** | ⭐ 70/100 | 一种去中心化的自优化虚拟处理器架构 | 通过运行时依赖分析实现自动并行化，具备工程实现。 | <details><summary>展开</summary>This work introduces a self-optimizing virtual processor (VP) for numerical array programs that shifts parallelization from a manual developer task to a cooperative, agent-like runtime mechanism. Instead of relying on centralized task-graph scheduling, static compiler optimization, or explicitly annotated parallel constructs, the VP uses a decentralized network of cooperative execution segments, derived from the stream of numerical instructions and their data dependencies at runtime. Each segment makes only local decisions about when, where, and how to prepare and execute its computation, including task placement, kernel preparation, and data movement. No central scheduler or mapper instance determines the execution globally; instead, scheduling itself is parallelized and distributed over time - asynchronously and strictly dependency driven. The overall execution strategy emerges from concurrently executing local segments, continuously responding to data availability, cost estimates, system state, hardware capabilities, and problem size. While preserving the sequential semantics of the program our VP automatically exploits parallelism across large program regions rather than being limited to individual loop bodies, modules, or explicitly marked parallel sections; developers are not required to design or encode a parallelization strategy. The current VP primarily targets low-latency strong scaling on local heterogeneous hardware, covering workloads from small, latency-sensitive array operations to large data-parallel computations. The current implementation targets the predefined array instruction set of the ILNumerics ONAL domain-specific language, accessible https://github.com/ILNumerics/ILNumerics.ONAL , while the underlying concept is applicable to general array-based numerical programming models such as MATLAB and NumPy.</details> |
| **[ACALSim: A Scalable Parallel Simulation Framework for High-Performance System Design Space Exploration](https://arxiv.org/abs/2605.22936v1)** | ⭐ 70/100 | 一种高性能并行架构仿真框架 | 架构仿真工具，具备良好的性能评估与实现，但非生产基础设施。 | <details><summary>展开</summary>Architectural simulation has become the critical bottleneck limiting design space exploration for high-performance computing systems. Modern GPUs and AI accelerators -- with hundreds to thousands of tightly-coupled components -- demand simulation frameworks that deliver efficient parallelism and scalable single-node execution. Existing frameworks fall short: SST focuses on multi-node MPI scalability but struggles with intra-node scaling, while GPGPU-Sim remains largely single-threaded. Critically, none expose a mechanism for users to optimize threading for their specific workloads. We introduce ACALSim, a scalable parallel simulation framework providing infrastructure and APIs for building high-performance simulators -- timing-model accuracy remains the responsibility of simulator developers. Its key innovation is a pluggable thread-management architecture that lets developers implement custom scheduling strategies tailored to specific simulation patterns, absent in existing frameworks. Complementing it are (1) event-driven execution with fast-forward to eliminate idle-cycle overhead, (2) a shared-memory data model enabling zero-copy communication, and (3) a two-phase parallel execution model for deterministic thread scaling. We demonstrate ACALSim through HPCSim, a GPU simulator targeting A100-class architectures. Against an SST implementation using identical shared timing cores to isolate framework overhead, ACALSim achieves over 14x speedup with 41% lower memory footprint; hardware validation confirms 0.72--1.22x cycle-count correlation with A100 measurements. While SST fails to complete 256+ thread-block workloads within practical time limits, ACALSim simulates full LLaMA transformer layers (single block) in 17.7 minutes for LLaMA-7B and 30.4 minutes for LLaMA-13B -- enabling design space exploration that SST cannot achieve.</details> |


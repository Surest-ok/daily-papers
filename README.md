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

## 2026-07-23

## OS Kernel & Scheduling

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[SuperPass: Fast-Tracking Blocking Threads to Mitigate Priority Inversion on Mobile Devices](https://arxiv.org/abs/2607.18097v2)** | ⭐ 88/100 | Android内核调度优化以缓解优先级反转问题 | 针对移动端调度痛点的工程实现，评估扎实且效果显著 | <details><summary>展开</summary>Priority inversion occurs when a high-priority thread is delayed by a lower-priority one. Although well studied in real-time systems, its impact in general-purpose OSes (e.g., Android) remains underexplored. On Android, we find that priority inversions happen frequently and can delay latency-critical threads, degrading user experience. For example, the foreground app's UI thread is frequently blocked by low-priority threads, with blocking durations of up to 210 ms, enough to cause dropped frames. Existing solutions designed for real-time systems fail to eliminate long priority-inversion blockings on latency-critical threads and may introduce high overhead on Android. To solve this problem, we uncover two insights on Android: 1) long blockings are mainly due to the accumulated CPU waiting time of low-priority blocking threads rather than their critical-section latency; and 2) although latency-critical threads can be blocked by many concurrent readers, tracking a limited number of them is sufficient to achieve good responsiveness with low overhead in most cases. Guided by these insights, we propose SuperPass, a lightweight kernel mechanism that mitigates priority inversion by fast-track scheduling of low-priority threads blocking latency-critical threads. It introduces a scheduler fast track that grants immediate CPU access to threads blocking latency-critical threads, and employs a lock-level detector that effectively identifies most such blocking threads. We evaluate SuperPass on a Google Pixel 8 smartphone. Taking UI thread as a case study, SuperPass decreases the 99.9th-percentile blocking duration by 72.0% and blocking count by 47.7% on average compared to the default scheduler, and reduces janky frames by 29.2% with a system-wide CPU overhead of only 0.74%. SuperPass also outperforms existing approaches including priority inheritance, real-time UI promotion, and Proxy Execution.</details> |

## File Systems & Storage

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[What Governs Decode Throughput in Absolute-Offset GPU LZ77? A Work-Granularity Mechanism and an Encode-Time Min-Match-Length Lever](https://arxiv.org/abs/2607.18541v1)** | ⭐ 82/100 | 通过调整LZ77最小匹配长度提升GPU解压吞吐 | 针对GPU存储性能的工程优化，实验扎实且可落地 | <details><summary>展开</summary>The ACEAPEX line of work established a lossless LZ77 format whose back-references are absolute output positions, giving parallel, compressed-resident GPU decode with sub-millisecond region seek. What it did not establish is what governs the decode throughput of such a format, or how to improve it. This paper answers both. Through controlled ablations on an NVIDIA H100 we show that decode throughput is governed not by occupancy, compute, address scatter, or launch parallelism, but by work granularity: throughput is a function of the average match length, because a short match leaves most lanes of a cooperating warp idle. A synthetic copy kernel confirms a 3.5x throughput span (212 to 744 GB/s) as average match length grows from 32 to 1024 bytes. Real data sit at the low end (mean match length 6.5 on enwik9, 10.1 on FASTQ). We then show that this mechanism yields a practical, encode-side lever: raising the minimum match length by distance class (6/8/10/12 to 12/16/24/32) improves both compression ratio and decode throughput simultaneously on all eight tested datasets, with no exceptions and no change to the decode kernel. FASTQ decode rises from 142.6 to 178.6 GB/s while ratio improves 1.8%; enwik9 throughput rises 78%. This is not a trade-off: both gains follow from one cause, removing short matches whose far offsets cost more entropy than they save. All figures are bit-perfect (FNV on GPU paths, byte compare on CPU paths) and git-verifiable. Scope is explicit: figures are match-phase, device-resident; entropy and host transfer are outside the timer; seek is read/block-level, not coordinate-level; and we do not claim to exceed the hardware bandwidth ceiling.</details> |

## Container & Virtualization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Isolation Failure From Shared Storage: Characterizing and Exploiting Page-Cache SCA Leakage Across Containers and VMs](https://arxiv.org/abs/2607.17518v1)** | ⭐ 82/100 | 揭示共享页缓存导致容器与虚拟机的侧信道泄露风险 | 深入分析多层隔离下的缓存侧信道，实验严谨且具工程价值 | <details><summary>展开</summary>Modern cloud platforms increasingly combine strong software isolation mechanisms with shared hardware resources to improve performance and resource efficiency. Conventional containers do this by sharing the host kernel directly, whereas sandboxed runtimes (e.g., gVisor) and VM-based runtimes (e.g., Kata, QEMU/KVM) provide progressively stronger isolation. In all cases, when tenants access host-backed filesystem state, the host page cache can remain shared and observable. Although OS-managed, this page-cache channel forms an OS-mediated microarchitectural timing side channel whose signal is shaped by the processor microarchitecture, memory and storage hierarchies, and virtualization mechanisms. We thus investigate whether unprivileged timing measurements can reveal page-cache residency across these isolation boundaries. Our evaluation covers Docker; gVisor with systrap and KVM; Kata Containers using QEMU and Cloud Hypervisor with shared host filesystems; Kata using QEMU, Cloud Hypervisor, and Firecracker with block-device-backed storage; and QEMU/KVM virtual machines under multiple host cache policies. Our results show that the timing signal persists whenever the I/O path exposes shared, host-cacheable file-backed objects, including under OverlayFS layers, virtio-fs exports, and loop-backed block devices. However, direct I/O and dedicated block devices substantially attenuate or eliminate the signal. Virtualization therefore reshapes leakage through added latency and algorithmic noise but does not remove the underlying dependence on shared hardware and cache state. We showcase this through a case study in which we recover coarse-grained activity from a WordPress deployment backed by MySQL. These results place page-cache attacks within the broader class of OS-mediated microarchitectural timing channels and motivate coordinated hardware, virtualization, and OS support for timing isolation.</details> |

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation](https://arxiv.org/abs/2607.19182v1)** | ⭐ 88/100 | 基于因果图与安全门控的K8s SLO自动修复系统 | 系统设计严谨，具备生产级安全机制，且开源评估充分。 | <details><summary>展开</summary>Maintaining service-level objectives (SLOs) on Kubernetes microservices remains difficult because autoscalers observe coarse resource metrics, recent SLO controllers often depend on custom telemetry, and unconstrained agentic operators cannot safely mutate production clusters. We present ARBITER, a guarded control plane for SLO-oriented Kubernetes remediation. ARBITER builds an OpenTelemetry-native causal resource graph, assembles bounded DiagnosisContext objects, and exposes a finite typed-action interface that separates planning from execution. The same interface supports deterministic planners and an LLM-backed planning harness, with deterministic schema checks, policy gates, resource/disruption budgets, approval, and bounded execution forming the safety substrate. We evaluate ARBITER on a 4-node Kubernetes cluster using DeathStarBench Social Network and Online Boutique. The evaluation tests two forms of SLO-oriented control that resource autoscaling alone does not provide: selecting the right remediation action and selecting the right downstream target. For bad-image deployment regressions, ARBITER selects rollback_canary in all ten CPU-burn and pure-latency runs; HPA either scales the faulty image or never triggers. For a downstream critical-path fault, the user-visible breach appears at the frontend, but trace evidence identifies home-timeline-service as the remediable bottleneck. Deterministic ARBITER and a live approval-gated Sonnet harness target that downstream service in every replicate, whereas HPA/resource-only control never does. Additional experiments cover guarded placement repair, Online Boutique portability, adversarial safety rejection, offline multi-model replay, and KWOK-based control-plane scale evidence. We release the controller, replay corpus, harnesses, safety tests, and figure artifacts: https://github.com/pooyan/arbiter.</details> |

## eBPF & Observability

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Enabling Multi-Dimensional Distributed Trace Comparison with Contrast](https://arxiv.org/abs/2607.19102v1)** | ⭐ 82/100 | 提出Contrast系统实现多维分布式链路对比分析 | 系统设计实用，在生产环境验证且评估扎实。 | <details><summary>展开</summary>Diagnosis using distributed traces is fundamentally a comparative task: operators seek to understand how an anomalous execution differs from expected behavior, how a deployment changes system execution, or how two individual executions differ. Trace comparison is challenging because useful differences between executions can manifest across multiple dimensions, and no single diagnostic interface is effective at capturing all of them. Moreover, the relevant dimensions and comparison populations are often not known a priori; operators construct and refine comparison sets dynamically as they develop hypotheses about system behavior. This paper presents Contrast, a system for multi-dimensional comparative trace analysis. Contrast introduces the Trace Projection Object (TPO), a mergeable representation that captures structural, temporal, critical-path, and semantic properties of trace populations while enabling efficient construction of arbitrary comparison sets at query time. Unlike approaches that define a fixed notion of trace difference, Contrast separates trace representation from comparison semantics, allowing diverse interfaces to selectively reason about specific dimensions. This separation enables the composition of complementary interfaces, allowing operators to combine insights from multiple dimensions for more effective diagnosis. We demonstrate this capability through two complementary interfaces: (i) SpectroViz, a critical-path-based visual interface for localizing execution differences; and (ii) Parallax, a natural language interface for generating explanations of trace differences using LLMs. We demonstrate the effectiveness and efficiency of Contrast through controlled experiments on traces from DeathStarBench and evaluation on production traces from Uber.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Quality over Quantity: Value-Driven Distributed Congestion Control for the Collective Perception Service](https://arxiv.org/abs/2607.18495v1)** | ⭐ 70/100 | 提出基于信息价值的分布式拥塞控制机制 | 针对车载网络拥塞的实用优化，评估较扎实 | <details><summary>展开</summary>While the Collective Perception Service (CPS) enables the exchange of sensor information among Intelligent Transport System Stations (ITS-S'), frequent transmission of Collective Perception Messages (CPMs), their highly variable size, and load from other vehicular services can cause severe channel congestion. Existing Distributed Congestion Control (DCC) Access layer mechanisms typically regulate channel load without considering the relative importance of the objects carried in CPMs. This limits their ability to preserve high-value information under constrained radio resources. More recently, Facilities layer DCC mechanisms attempt to prioritise high value objects within the specified radio resource limits but may not operate well in heterogeneous environments where the number of sensed objects and their importance can vary significantly over time or between ITS-S'. This paper proposes a value-based DCC Facilities layer 'quality' selector that couples a Value of Information (VoI) per bit rate controller with object-level selection. It is benchmarked against state of the art approaches from standards and the literature, with results showing that the proposed method maintains channel load near the target CBR while retaining more high-VoI objects than state of the art approaches, thereby improving the dissemination of perception-critical information.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Unstructured Hydrodynamics on Spatial Dataflow Architectures: A Joint Code and Data Decomposition Approach](https://arxiv.org/abs/2607.18650v1)** | ⭐ 75/100 | 非结构化网格在空间数据流架构上的高效映射 | 针对特定硬件的架构优化，具备实际性能评估。 | <details><summary>展开</summary>Spatial Dataflow Architectures are an emerging hardware pattern in high-performance computing, whose mesh-connected fixed-memory processing elements are tailored for structured grid kernels with two-dimensional neighborhoods. However, practical multiphysics codes are often computed on unstructured grids, which induce indirect memory accesses and high-dimensional communication patterns, making them infeasible to directly map onto said architectures. This work takes a principled, model-centric approach to partitioning unstructured problems onto spatial dataflow architectures. Through communication and memory modeling, we propose a joint decomposition that considers both the size of the application's fields and its subroutines. In particular, we automate the analysis process of the original code, define a high-dimensional decomposition that minimizes communication via space-filling curves, and apply memory optimization techniques, crucial in this memory-limited environment. We demonstrate mapping the Livermore Unstructured Lagrangian Explicit Shock Hydrodynamics (LULESH) application to the Cerebras Wafer-Scale Engine, showing that larger, unstructured grid codes can still outperform GPUs.</details> |


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

## 2026-08-22

## OS Kernel & Scheduling

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Performance Verification of the AmpereOne CPU Core](https://arxiv.org/abs/2608.19300v1)** | ⭐ 75/100 | AmpereOne CPU性能验证方法论 | 工业级CPU验证方法，工程实践价值高，但偏硬件设计。 | <details><summary>展开</summary>As process technology scaling slows, microarchitectural innovation has become the primary driver of performance gains, making pre-silicon Performance Verification (PV) more critical than ever. This paper presents the industrial-scale PV methodology applied across four generations of the AmpereOne custom CPU core, centered on the cycle-accurate correlation of the RTL design against a trace-driven performance model. The methodology integrates data-driven workload curation, a high-frequency daily regression system, and a unified event-stream framework for analysis. We demonstrate this methodology through case studies of the Branch Prediction Unit and L2 Prefetcher, highlighting a hierarchical strategy that first isolates individual units for focused correlation before proceeding to full-core verification. The results demonstrate that this disciplined, iterative process is indispensable for avoiding costly post-silicon bugs and ensuring complex processors meet their performance targets. We end with a look towards the future of PV in the microprocessor industry.</details> |

## File Systems & Storage

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Design and Empirical Evaluation of a Network-Centric, On-Premises Architecture for Earth Observation Data Access](https://arxiv.org/abs/2608.20283v1)** | ⭐ 82/100 | 构建高性能地球观测数据存储与网络架构 | 基于真实生产环境的存储与网络性能实测，工程价值高。 | <details><summary>展开</summary>Earth observation (EO) programmes generate data at volumes that exceed the transfer and storage capacity of most institutional networks. Public cloud platforms address this for well-resourced organisations, but institutions across the Atlantic basin face constraints in connectivity, sovereignty and funding that make on-premises infrastructure the only viable path. Cloud-native data formats enable efficient partial reads, yet their performance depends on the bandwidth of the underlying network fabric, a dependency rarely measured in isolation. This paper presents a replicable, network-centric architecture for on-premises EO data access, evaluated at its first operational deployment: the AIR Data Centre, founding node of the Atlantic Cloud. The system comprises a MinIO object storage cluster on a 100 GbE fabric, a PostGIS metadata catalogue and an OGC API-EDR access layer. We characterise the fabric under sustained parallel load, evaluate object storage throughput for EO-representative workloads, and compare measured performance against throttled baselines on identical hardware, isolating network bandwidth as the sole variable. Multi-site replication benchmarks with partner institutions characterise the federation primitive the model depends on. Network bandwidth is the dominant constraint on storage throughput for bulk EO data access up to a threshold; beyond it, endpoint memory topology rather than capacity governs how much bandwidth a system can use. For this hardware class that threshold lies above 10 Gbps per server. Below it, network capacity alone sets what the facility can deliver; above it, the return on further network investment depends on endpoint memory provisioning, which can be deferred and bought later.</details> |

## Container & Virtualization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[The Lazy Pod That Lies: Deferred Cost and Failure Semantics of Lazy Container Image Pulling for Model Serving on Kubernetes](https://arxiv.org/abs/2608.19412v1)** | ⭐ 88/100 | 揭示容器懒加载机制的性能代价与生产环境故障风险 | 深入分析生产级容器懒加载系统的性能与稳定性缺陷，极具工程参考价值。 | <details><summary>展开</summary>Lazy container-image pulling promises to eliminate the dominant cost of starting a model-serving pod by mounting the image immediately and fetching content on demand. We evaluate this promise for model delivery on Kubernetes, using KServe with two production lazy-pulling systems -- eStargz/stargz-snapshotter and AWS SOCI -- against eager baselines, on artifacts from 2 to 140 GB including real fp16 weights. Lazy pulling delivers its headline: cold time-to-first-prediction becomes size-independent (16.9--17.6s, versus 24.5--573.0s eager). But the cost is deferred, not eliminated: a full read of a 14 GB model through the lazy mount takes 105.3s, slower than the 72.4s eager pull it replaced, and the two systems pay at opposite lifecycle ends (SOCI prefetches nearly the full image before Ready; eStargz defers nearly everything to first read). More consequentially, we characterize a failure mode eager pulling structurally cannot exhibit: under sustained legitimate reads with default configuration, the snapshotter's node-level cache exhausts its finite volume and already-running pods begin failing reads of model files. At the earliest stage of exhaustion, an instrumented serving pod passed every Kubernetes-visible and application-level check for 196s while its snapshotter was already logging real failures; under heavier pressure, 67--94% of model files fail, scaling monotonically with residual cache occupancy. A live pod self-heals if cache space is freed under it, but a snapshotter-daemon restart under a live pod leaves permanently stale file handles in a pod still reported Running. We derive placement, monitoring, and cache-sizing guidance for serving platforms and operators.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Empirical Evaluation of Cross-Carrier MCPTT & OTT MCX Interoperability in High-Density Environments](https://arxiv.org/abs/2608.19554v1)** | ⭐ 78/100 | 评估高密度场景下MCPTT跨运营商互操作性与QoS表现 | 在真实大型赛事中进行实地测试，对网络拥塞下的语音质量与传输层抖动提供了宝贵的工程实证。 | <details><summary>展开</summary>Deploying broadband Mission-Critical Push-To-Talk (MCPTT) services over shared commercial infrastructures introduces resource contention during multi-agency responses in mass-crowd events. This study evaluates cross-carrier interoperability and standard versus prioritized quality of service (QoS) frameworks under real-world saturation constraints. We design an empirical multi-carrier field experiment utilizing twelve identical smartphones deployed across multiple physical sectors inside Texas A&amp;M University's Kyle Field during a football game with 105,000+ attendees. Automated voice calls were monitored using Perceptual Objective Listening Quality Analysis (POLQA), packet delivery metrics, and connection rates. The results reveal that voice path failure is isolated to network infrastructure bottlenecks rather than device hardware limitations. Specifically, we identify a sharp, non-linear network failure model where transport-layer jitter exceeding a critical threshold de-jitter buffer underflows, causing structural audio degradation. Priority-managed channels effectively bypass this congestion. This study helps establish an operational insight for emergency planners to mandate network infrastructure, end-to-end network slicing and dedicated resource provisioning capable of keeping transport-layer jitter below the critical failure boundary.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[ParaWeb: Parallel Programming Patterns for Web Development](https://arxiv.org/abs/2608.19935v1)** | ⭐ 82/100 | 提供Web端并行编程模式库以提升计算性能 | 实现实用且高性能的并行模式，评估详尽，工程价值高 | <details><summary>展开</summary>Modern web applications increasingly require computationally intensive processing, yet JavaScript, the dominant language of the web, has traditionally been limited to a single-threaded execution model. Node.js Worker Threads and browser Web Workers provide low-level mechanisms for parallel execution, but developers lack high-level abstractions that capture recurring parallel structures as reusable patterns. In this paper, we present ParaWeb, a TypeScript library that implements ten parallel programming patterns for server-side Node.js, client-side browser environments, and WebGPU compute shaders. ParaWeb provides three implementation variants for each pattern: a message-passing (MP) variant based on structured cloning via postMessage, a shared-buffer (Shared) variant that uses SharedArrayBuffer with typed array views, and a GPU variant that uses WebGPU compute shaders for hardware-accelerated execution. We describe the architecture, design decisions, and pattern-specific implementation strategies, and we evaluate the performance of all thirty implementations across three data sizes. Experimental evaluation results show that the CPU-based variants achieve speedups of up to 11.6x with 16 threads for compute-bound patterns, while the GPU variants reach speedups of up to 260x for compute-bound patterns with high arithmetic intensity such as Farm, Scatter, Reduce, and Map. A case study on five image-convolution filters further shows that GPU acceleration reaches up to 414x speedup over single-threaded CPU on non-separable kernels, with consistent scaling across 1024x1024$, 2048x2048$, and 4K images.</details> |


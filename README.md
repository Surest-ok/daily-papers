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

## 2026-07-03

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[MeshDNS: A Cooperative DNS Resolution Framework for Resource-Constrained IoT Networks](https://arxiv.org/abs/2607.00122v1)** | ⭐ 78/100 | 面向IoT网络的去中心化DNS解析框架 | 在ESP8266上实现并验证，具备高实用性与鲁棒性 | <details><summary>展开</summary>Domain Name System (DNS) resolution in Internet of Things (IoT) networks presents unique challenges due to resource constraints, unreliable connectivity, and security vulnerabilities. Traditional centralized DNS architectures introduce single points of failure. This paper presents MeshDNS, a cooperative DNS resolution framework designed for resource-constrained IoT environments operating under shared-key admission. MeshDNS employs a decentralized architecture where nodes maintain cache awareness using hash-based summaries and secure cold-cache misses via Ed25519-signed, identical-answer quorum voting. Our implementation on commodity ESP8266 microcontrollers (sub-50 KB usable RAM, 80 MHz) achieves a 0.47 ms warm-cache resolution, outperforming native mDNS baselines (1.39 ms). To secure initial cold-cache misses, MeshDNS trades a predictable ~1.3-1.7s cryptographic penalty to successfully isolate Byzantine faults among admitted peers. Assuming a threat model where physical hardware extraction remains out of scope, MeshDNS demonstrates Byzantine fault isolation. We validated the framework via a 5-node physical testbed and discrete-event simulations scaling to 1,000 nodes; the results demonstrate that MeshDNS maintains resilient local name caches for persistent edge telemetry under network churn. Code is available at https://github.com/mahbubasif/MeshDNS-Artifact.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Promise-Future Synchronization for Cluster Asynchronous Many-Task Runtimes via MPI One-Sided Communication](https://arxiv.org/abs/2607.00303v1)** | ⭐ 75/100 | 引入Promise-Future模型提升AMT运行时动态任务调度能力 | 通过MPI单向通信优化运行时，实验验证了扩展性与性能提升 | <details><summary>展开</summary>Asynchronous Many-Task (AMT) runtimes use futures as placeholders for values produced by other tasks. In the ItoyoriFBC AMT runtime, the existing future-only model binds each future to its producer at creation time and requires the number of tasks that read each future to be fixed at compile time. This prevents directly expressing algorithms that create dependencies dynamically. We extend ItoyoriFBC with an implementation of a promise-future model that lifts these limitations. Thereby, our ItoyoriFBC variant supports dynamic algorithms such as Hierarchical LU factorization (HLU). We experimentally evaluated our implementation using HLU on up to 16 nodes and observed near-ideal scaling with a 15.6x speedup.</details> |
| **[Five Ways to Build a Concurrent Linked From Coarse-Grain Locking to Lock-Free Algorithms](https://arxiv.org/abs/2606.28972v1)** | ⭐ 75/100 | 对比五种并发链表实现并评估性能表现 | 通过C++实现并进行多场景基准测试，实用性强 | <details><summary>展开</summary>Linked lists are one of the most basic data structures in computer science. But when many threads try to use the same linked list at the same time, things get complicated. In this paper, we look at five different ways to make a linked list work correctly and efficiently with multiple threads running at once. We start with the simplest approach -- one big lock for the whole list -- and step by step improve it, ending with a lock-free design that uses no locks at all. We implemented all five versions in C++ and measured how fast each one is across different workloads (read-heavy, balanced, and write-heavy) and different list sizes. Our results show that the right choice of algorithm depends heavily on how the list is used: the coarse-grain and lazy lists win under read-heavy workloads with small key ranges, while the lock-free list becomes competitive when key ranges are large and more threads are running. Fine-grain locking, despite its theoretical appeal, pays a heavy cost from per-node lock overhead and consistently performs the worst in our tests.</details> |
| **[SchedCheck: Schedule-Robustness Analysis for Event-Driven Block Programs](https://arxiv.org/abs/2607.00623v1)** | ⭐ 75/100 | 针对块编程语言的并发调度鲁棒性分析工具 | 针对Scratch VM的调度分析，方法严谨且有实测数据，符合系统工程范畴。 | <details><summary>展开</summary>Block-based languages such as Scratch let beginners assemble interactive programs from sprites and scripts. These programs are concurrent in practice: green-flag scripts, broadcasts, and clones run as cooperatively scheduled threads over shared sprite and stage state, and their authors never write a thread. We show that such programs contain schedule-sensitive behaviors whose observable result depends on an execution order the language leaves open. Editing, saving, or remixing a project can produce a copy with the same blocks but a different layer order, changing the order the virtual machine starts scripts. We formalize the schedule space a Scratch virtual machine can realize as the permutations of the initial executable-target order, and define schedule-robustness against a lattice of observation lenses over a fixed horizon. A partial-order exploration runs one schedule per dependence-equivalence class, and on projects small enough to enumerate, an independent oracle confirms it recovers every realizable outcome. On larger projects, representatives stand in for the factorial under the validated dependence model. SchedCheck implements this on the production Scratch VM. Across 224 real student projects, at least 21% of the concurrent ones are schedule-sensitive at the grading lens, and a uniform random sample of public projects replicates the rate at 17.6%, with two real remixes of a deployed animation arranging its letters differently. On hand-built fault pairs and a generated benchmark of 32 spec-defined faults across four classes, the tool detects and localizes every schedule fault, with a logic-fault control reporting clean. The oracle exposed four unsoundness gaps in the dependence model, all repaired. The method is parametric in the execution model, instantiating unchanged on a second cooperative event loop.</details> |


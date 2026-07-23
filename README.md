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

## 2026-07-24

## File Systems & Storage

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Black-Box Performance Evaluation of Elastic Block Storage: Contract, Rate-Limiting Model, and Software Exploration](https://arxiv.org/abs/2607.20319v1)** | ⭐ 82/100 | 揭示云端块存储特性并优化应用性能 | 实测数据详实，对云存储性能优化有直接指导意义 | <details><summary>展开</summary>Elastic block storage (EBS) with the storage-compute disaggregated architecture is a key component in modern cloud infrastructure. EBS offers users storage resources in the form of elastic solid-state drives (ESSDs). Nonetheless, despite recent efforts that have documented EBS architectures from the provider's perspective, how ESSDs perform differently from local SSDs and how host software should adapt accordingly have not been sufficiently studied. In this paper, we conduct a user-centric, black-box performance characterization of ESSDs from Amazon AWS and Alibaba Cloud. We make three main contributions: (1) an ESSD contract that presents four behavioral observations and five actionable implications for software adaptation, (2) a refined I/O rate-limiting model combining bandwidth-IOPS dual limiting and fine-grained token refilling to suppress latency spikes, and (3) a case study on RocksDB that derives four guidelines on cache management, I/O regulation, storage budget utilization, and compression algorithms. Collectively, we hope these contributions can serve as a practical reference for EBS users to understand and exploit the distinctive performance properties of ESSDs.</details> |

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[SequenceFI: Non-intrusive Temporal Fault Injection for Microservice Systems](https://arxiv.org/abs/2607.20050v1)** | ⭐ 88/100 | 微服务系统非侵入式时序故障注入框架 | 系统实现完善，评估扎实，具备极高的工程实用价值。 | <details><summary>展开</summary>Fault injection is widely used to evaluate the resilience of microservice systems, where client requests often span multiple services and execution stages. Existing request-level techniques usually control where and what faults are injected, but not when they are activated within a distributed execution. This limitation makes it difficult to reproduce timing-dependent failures, such as failures after state-changing side effects, order-sensitive concurrent responses, and partial failures among repeated downstream calls. This paper presents SequenceFI, a non-intrusive framework for temporal fault injection in microservice systems. SequenceFI observes message-level send and receive events, propagates compact temporal evidence along request executions, and triggers faults only when occurrence-sensitive temporal guards are satisfied. It further synthesizes temporal guards from traces, reducing the need for exhaustive enumeration of temporal fault-injection configurations, while requiring no modifications to application code or serialization libraries. We implement SequenceFI on Kubernetes and evaluate it on four widely used microservice benchmarks. Across nine temporal-fault scenarios and 450 valid trials, SequenceFI achieves 100.0\% temporal success without premature or multiple injections, finds effective configurations in one attempt on average, and reduces aggregate end-to-end search time by 95.91\% compared with H-Random.</details> |
| **[Examining QRMI as a Unified Interface for Quantum-HPC Integration](https://arxiv.org/abs/2607.19591v1)** | ⭐ 78/100 | 提出QRMI中间件实现量子计算资源在多调度器下的统一管理 | 通过多调度器集成验证了接口的通用性与工程实用价值 | <details><summary>展开</summary>The efficient and scalable integration of quantum resources into high-performance computing (HPC) environments requires standardized mechanisms for resource management, scheduling, and workflow orchestration across diverse and heterogeneous infrastructures. The Quantum Resource Management Interface (QRMI) addresses this challenge through a thin, vendor-agnostic middleware layer that provides standardized APIs for scheduling, executing, and monitoring quantum workloads while exposing quantum resources as first-class schedulable resources alongside CPUs and GPUs. Although previous work demonstrated QRMI integration with the Slurm workload manager, its applicability across other workload managers remained unexamined. This paper extends the validation of QRMI to a broad range of workload managers, including PBS, LSF, Grid Engine, Kubernetes, and the Flux Framework, encompassing traditional batch schedulers, a cloud-native orchestration platform, and a graph-based scheduler. We examine the integration patterns, implementation requirements, and scheduler-specific considerations associated with each environment and compare QRMI with alternative approaches to quantum resource integration. We demonstrate that QRMI provides a portable and flexible abstraction layer that minimizes scheduler-specific modifications while enabling consistent access to heterogeneous quantum resources across both on-premises and cloud environments.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[SRAN: Scaling Named Data Networking via Map-and-Encap](https://arxiv.org/abs/2607.20363v1)** | ⭐ 78/100 | 提出SRAN架构，通过映射封装实现NDN路由扩展 | 架构设计合理，通过映射解耦提升了NDN的可扩展性。 | <details><summary>展开</summary>Network routing scalability is hard to achieve when forwarding state is driven by external entities such as end users or multicast groups. Named Data Networking (NDN) faces this challenge acutely: it fetches data by name, which ties forwarding state to an unbounded number of application name prefixes. This paper presents SRAN, a scalable routing and forwarding architecture for NDN. Building on the Map-and-Encap principle, SRAN separates name-prefix reachability from topological reachability by mapping prefixes to egress routers at the network edge. Consequently, the network core routes and forwards based solely on topological connectivity. SRAN extends this mapping to support multicast by adapting Bit Index Explicit Replication (BIER), encoding prefix-to-multiple-egress mappings as a BitString to enable stateless multicast delivery. Implemented on the NDN substrate, SRAN leverages NDN's native security and dataset synchronization for secure routing and prefix-state dissemination, requiring no additional protocol. Evaluation on representative Rocketfuel topologies confirms that the network forwarding state scales with the topology rather than the application-prefix count, and adapts to prefix changes in real time with minimal dissemination overhead.</details> |
| **[Scalable Multi-Controller Coordination in Periplus via Border-Switch Forwarding Graphs](https://arxiv.org/abs/2607.19508v1)** | ⭐ 78/100 | Periplus实现带内SDN多控制器高效协同 | 方案工程可行性高，通过边界交换机转发图优化扩展性 | <details><summary>展开</summary>In-band SDN control planes, where control traffic shares the data-plane infrastructure, suit wide-area, resource-constrained deployments -- such as rural backbones -- that cannot afford a dedicated control network. Partitioning such a network across multiple controllers improves scalability but raises a coordination challenge that in-band designs have largely ignored: controllers must discover one another and exchange state in-band, and switches must recover when their controller fails, all without forwarding state that grows with the number of controllers. This paper presents the multi-controller coordination plane of Periplus, an in-band control plane whose single-controller design is developed in a companion paper. Periplus controllers discover their neighbors through Controller Advertisement (C-Adv) messages and build inter-controller routes incrementally: each border switch inserts a partial forwarding graph covering only the next domain, so per-controller forwarding state is confined to border switches and never distributed across the interior of an intermediate domain. The same C-Adv mechanism reattaches a switch to a surviving controller after a controller failure. We evaluate a Ryu-based implementation in Mininet, including a 96-switch, 5-controller scenario. Per-switch flow-table state is set by a switch's role rather than by network size -- interior occupancy stays constant as controllers are added -- partitioning scales bootstrap to networks of around a hundred switches, and inter-controller discovery converges within seconds. The design needs no switch-firmware modifications: it runs on stock Open vSwitch, using only its built-in Nicira extensions for Network Service Header (NSH) encapsulation.</details> |


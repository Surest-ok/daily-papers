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

## 2026-09-12

## Container & Virtualization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Memory Compression for High-Fanout Agent Sandboxes](https://arxiv.org/abs/2609.11294v1)** | ⭐ 78/100 | 针对AI代理沙箱的内存压缩系统 | 利用沙箱间冗余优化内存，工程实现扎实且评估充分 | <details><summary>展开</summary>High-fanout agent workloads create a growing memory bottleneck because a single task may spawn many concurrent sandbox sessions. Yet these sandboxes are far from independent: they originate from a shared template and execute related trajectories, exposing substantial template-relative and cross-sandbox memory redundancy. Conventional memory compression is poorly matched to this setting in three fundamental dimensions: how to compress, because they fail to exploit similarity across non-identical sandbox pages; what to compress, because they control page-fault overhead through conservative page selection; and when to compress, because compression is either triggered by memory pressure or performed without awareness of agent execution phases. We present AgentZip, the first memory compression system designed specifically for AI-agent sandboxes. AgentZip introduces compression mechanisms that exploit both the template-relative and cross-sandbox redundancy. It broadens the compression scope to any page with a profitable representation and shifts overhead control from compression-time page selection to restore-time prefetching. It further aligns expensive compression with LLM waiting periods to avoid interfering with foreground tool execution. Across LLM training and inference workloads, AgentZip reduces sandbox-owned memory by up to 8.7x, compared with 2.1x for the Linux configuration. Restore prefetching and agent-execution-aware scheduling reduce the slowdown of aggressive compression from as high as 3.1x to 1.40x while retaining nearly all of its memory-saving benefit.</details> |

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Composable CXL Memory as a Kubernetes-Native Shared Memory for LLM Serving](https://arxiv.org/abs/2609.10790v1)** | ⭐ 82/100 | 基于CXL的K8s共享内存KV缓存方案 | 利用CXL实现跨节点内存共享，工程实现完整且评估扎实 | <details><summary>展开</summary>We present a Kubernetes Dynamic Resource Allocation (DRA) driver that makes composable CXL memory a schedulable cluster resource, and evaluate the resulting shared-memory tier for cross-node KV-cache reuse in LLM serving. The driver composes CXL regions on demand, materializes them as DAX devices on each participating host, and injects them into pods under a single Container Device Interface (CDI) name so that pods on different nodes access the same physical region. A shared-memory connector for vLLM/llm-d uses that region as a KV-cache tier with a slot directory embedded inside the shared medium, which eliminates the need for an external metadata service. On a two-node cluster with a 512\,GiB CXL appliance and Qwen2.5-7B-Instruct, cross-node prefix reuse reduces TTFT by 5.5$\times$--36.6$\times$ at an external hit rate of 95.4--99.5\,\%, while node-local tiers (GPU prefix caching, CPU-DRAM offload) fall back to full recompute. The sharing gap, defined as the latency ratio between cross-node and same-node reuse, is 1--4\%, indicating that cross-node reuse incurs little additional latency relative to same-node reuse on our testbed. Both replicas run full engines; the study demonstrates memory disaggregation rather than prefill/decode disaggregation. We report this as a feasibility study rather than a performance evaluation.</details> |
| **[A Model-Centric DevOps Architecture for DEVS-Based Digital Twin Simulation Services](https://arxiv.org/abs/2609.11122v1)** | ⭐ 70/100 | 提出DEVS数字孪生DevOps架构 | 将CI/CD引入数字孪生模型管理，工程实践性较强。 | <details><summary>展开</summary>Digital twin simulation models are evolved and redeployed like software, yet DEVS-based engines offer a sound formal basis with little support for versioning, automated validation, or continuous delivery in cloud-native environments, leaving model lifecycle management ad hoc in most deployments. This paper proposes a model-centric DevOps architecture for deploying DEVS-based digital twin simulations as managed services. Simulation models are treated as first-class DevOps artefacts defined in a declarative YAML language with a formal mapping to multiPDEVS, supporting structural and semantic validation in a CI/CD pipeline that produces immutable versioned artefacts, so that reverting to an earlier validated version reduces to pinning its identifier. The platform is decomposed into containerised microservices on Kubernetes, with engine adaptations for state externalisation and lifecycle control. An initial case study on the Riga Route 22 public-transit corridor, the first instantiation of a planned city-wide multi-modal transport digital twin for Riga, Latvia, exercises the full lifecycle and reports single-container engine throughput for a scenario with roughly 47,870 DEVS atomic components; pipeline-level catch statistics and cluster-level concurrent multi-scenario execution are the subject of companion empirical studies.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[IPv6 Hitlist Service: Lessons Learned From 10 Years of Operation](https://arxiv.org/abs/2609.11475v1)** | ⭐ 78/100 | IPv6地址扫描服务十年运营经验与覆盖率分析 | 基于十年真实运营数据的系统性评估，实用价值高。 | <details><summary>展开</summary>After becoming an Internet Draft more than 30 years ago, IPv6 has seen an increase in deployment and use in the past years. As measurements in the IPv6 Internet require new approaches due to the vastly larger address space, hitlists have come along as one possible source for finding IPv6 targets. One of the most prominent hitlists is provided by the IPv6 Hitlist Service. In this paper, we share insights from 10 years of operations of the IPv6 Hitlist Service: We show different evolutions of the service, highlighting important changes along the way. To better understand the representativeness of the hitlist, we perform a coverage analysis using real-world traffic data from a major central European ISP and Tier-1 network, finding that at least one address is known to the IPv6 Hitlist Service for 87.1 % of ASes and 56.5 % of /48 prefixes originating IPv6 traffic. We also share results from a conducted user survey and analyze users accessing the IPv6 Hitlist Service, finding diverse use cases and access patterns across time (e.g., one-off vs. continuous downloads) and available data (e.g., all vs. responsive addresses). Finally, we provide best practice recommendations when working with the hitlist and share lessons learned during its 10-year operation.</details> |
| **[terms.txt: A Consent and Compensation Protocol for Agentic Web Access](https://arxiv.org/abs/2609.11152v1)** | ⭐ 78/100 | 提出terms.txt协议以规范AI爬虫访问与付费 | 协议设计实用且具备低开销实现，符合基础设施规范 | <details><summary>展开</summary>The open web ran on an unwritten bargain: sites admitted crawlers, and search engines sent visitors back. Public measurements show that bargain breaking under AI crawlers and agents. Automated clients now make up most requests, training dominates Cloudflare-classified crawling, and the largest AI platforms fetch thousands of pages for each visitor they return. The web's common control, robots.txt, cannot express identity, purpose, terms, or price, can be circumvented, and newer alternatives are largely proprietary CDN features. We specify terms.txt, a robots.txt-style file for per-path, per-purpose machine-access terms, plus an origin-enforced exchange using Web Bot Auth signatures, signed intent, delegation tokens, HTTP 402 negotiation, and signed receipts. We define what the exchange can enforce, audit, and leave to contract. A dependency-free implementation adds 0.20 to 0.65 ms per request on one vCPU.</details> |
| **[An FPGA-in-the-Loop Testbed for MU-MIMO OFDM Beamforming over Ray-Traced Wireless Channels](https://arxiv.org/abs/2609.06812v1)** | ⭐ 75/100 | 基于FPGA与数字孪生的MU-MIMO波束赋形测试床 | 通过硬件在环技术弥补了仿真与实机部署的差距，工程价值高。 | <details><summary>展开</summary>Wireless networks face ever expanding throughput demands from heterogeneous, high-density user populations, requiring beamforming algorithms that adapt to channel conditions with low latency. Validating such algorithms requires either costly over-the-air testbeds or simulation environments that lack the timing and resource constraints of real hardware, leaving a gap between algorithm design and hardware-realizable deployment. This work presents a hardware-in-the-loop (HIL) testbed that closes that gap by coupling an FPGA-based implementation of OFDM Waveforms with MU-MIMO beamforming to NVIDIA Sionna's ray-tracing channel simulator, enabling a physical base-station architecture to transmit and receive against a Sionna-rendered digital-twin propagation environment in real time. Unlike prior work that validates beamforming algorithms either purely in simulation or on full RF testbeds, this architecture allows beamforming logic running on actual FPGA fabric to be evaluated under realistic, controllable, and repeatable channel conditions, including UE mobility and site-specific multi-path, without requiring an anechoic chamber or live RF front end. We detail the FPGA OFDM transmit/receive pipeline, the synchronization and data interface between the FPGA and the Sionna environment, and validation of signal quality under AWGN and ray-traced channel conditions, establishing this testbed as a platform for hardware-validated beamforming research.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Rethinking Sparse Formats for RISC-V: A Hierarchical Approach to High-Performance SpMV](https://arxiv.org/abs/2609.11352v1)** | ⭐ 78/100 | 提出HCSR格式提升RISC-V架构下SpMV性能 | 针对RISC-V架构优化稀疏矩阵计算，实验扎实且开源 | <details><summary>展开</summary>The sparse matrix-vector multiplication (SpMV) algorithm is a fundamental computational kernel of linear algebra and serves as a building block for numerous applications, primarily iterative solvers for systems of linear equations used in scientific and engineering simulations. This paper compares vectorized implementations of the SpMV algorithm across eight established sparse matrix storage formats and proposes a novel modification of the CSR format, Hierarchical CSR (HCSR), which enhances SpMV performance on RISC-V processors. Our SpMV implementations utilize RVV 1.0 intrinsics and are publicly available as an open-source C++ library named RVVLASparse. Computational experiments conducted on SpacemiT K1 and K3 RISC-V boards demonstrate that selecting an appropriate matrix storage format accelerates SpMV computations by an average of 1.6x, while the proposed HCSR format achieves the shortest execution time among all considered formats across a broad class of sparse matrices.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[You've Got a BUD in Me: Authenticated Reads from Per-Block Write Logs](https://arxiv.org/abs/2609.11251v1)** | ⭐ 78/100 | 基于写日志的区块链高效验证方案 | 通过分层摘要优化了区块链状态读取性能，工程实现扎实。 | <details><summary>展开</summary>Blockchains usually pay for authenticated reads by maintaining a structure that spans the entire state. We show how validators can support historical membership and exclusion proofs by authenticating each block's writes instead. A Block Update Digest (BUD) commits a write log whose predecessor pointers link successive modifications of each key. A SuperBUD summarizes last writes over a window; an exponential hierarchy turns long unchanged intervals into short proofs. The digest count is logarithmic in the gap within the hierarchy's range, with one additional digest per top-level window beyond it. We prove soundness against adversarial provers and up to f Byzantine validators, and completeness for queries anchored by a post-deployment modification, assuming archive, attestation, and committee evidence is available. Across a 50x increase in state size, the measured base-BUD path rises by 1.24x, compared with 3.1x and 69.5x for in-memory and cache-bounded disk-backed Merkle Patricia tries. On the synthetic trace, two-digest read-layer payloads stay below 800 bytes, and warm hash-path verification takes at most 146 microseconds at p99.</details> |


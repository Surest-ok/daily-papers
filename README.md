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

## 2026-07-22

## File Systems & Storage

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Hardware-Transparent I/O Governance in Disaggregated Heterogeneous Storage](https://arxiv.org/abs/2607.16578v1)** | ⭐ 92/100 | Oracle Exadata存储I/O治理系统 | 生产环境部署，解决了异构硬件下的I/O调度难题 | <details><summary>展开</summary>Shared-nothing disaggregated storage clusters that serve both latency-sensitive databases and opaque block-volume workloads face two governance problems unsolved by existing schedulers: maintaining consistent performance across heterogeneous hardware generations, and enforcing global I/O limits when access patterns skew to a subset of storage nodes. We present the I/O Resource Manager (IORM), a multi-stage distributed scheduler deployed in production within Oracle Exadata Exascale. IORM combines three mechanisms: a hardware-aware cost modeler that normalizes I/O accounting using datasheet-derived fixed costs to make limits invariant across hardware generations; a quantum-based rate limiter with bounded carry-forward credits that accommodates database micro-bursts while enforcing long-term SLOs; and a distributed adaptive feedback controller that redistributes unused entitlements across the cluster to resolve topological access skew. Beyond design, we share operational lessons from production deployment. On an 8-node test cluster running up to 100 concurrent tenant volumes, IORM converges within 5\% of provisioned limits under extreme sequential skew, scales without inter-tenant interference, and recovers full throughput within 15 seconds of a storage-node failure.</details> |

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity](https://arxiv.org/abs/2607.16596v1)** | ⭐ 88/100 | 利用OCI镜像机制优化K8s模型加载冷启动 | 针对K8s模型分发痛点，提供了生产级实现与性能对比 | <details><summary>展开</summary>The startup latency of a model-serving pod on Kubernetes is dominated by one step: delivering the model weights. As models reach the hundred-gigabyte weights of large language models, cold-start delivery time governs the economics of autoscaling and scale-to-zero, yet the dominant mechanisms remain ad-hoc downloads from object storage, with none of the pull caching, digest addressing, or verification Kubernetes provides for container images. We analyze the delivery paths available to a Kubernetes serving platform along two axes: which component pulls the artifact, and whether any admission-time verifier can bind the deployed reference to the arriving bytes. We validate the analysis upstream in KServe, a widely deployed CNCF model-serving platform, by implementing two new delivery paths: oci+native://, which mounts model images as Kubernetes image volumes (KEP-4639), merged upstream, and oci+fetch://, which pulls OCI artifacts inside the storage initializer, under review. We report, to our knowledge, the first controlled comparison of model delivery paths in a Kubernetes serving platform (modelcar sidecars, native image volumes, object-storage download) on artifacts sized to fp16 weights of 1B-, 7B-, and 70B-class models (2-140 GB). Node-cached OCI delivery makes warm replica addition size-independent: 11.7 s for a 70B-class artifact versus 40.7 minutes of re-download over object storage, a 208x difference, while the first cold pull costs up to 2x a plain download, localized to containerd's blob-write-then-unpack double pass. For models on s3://, gs://, or hf:// URIs, where no admission-time verifier observes the bytes, we present a serving-time integrity design proposed to the KServe community: digest pinning and OpenSSF model-signing enforcement in the storage initializer. Streaming hash verification during download adds under 0.1% to delivery time; a post-download pass adds up to 53%.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Rethinking Polling Efficiency in Service Core Network Stacks](https://arxiv.org/abs/2607.16408v1)** | ⭐ 82/100 | 提出基于功耗预算的网卡核心调度策略 | 深入分析硬件功耗限制，对网络栈调度有实际指导意义 | <details><summary>展开</summary>Idle network service cores are treated as wasted compute. This assumption motivates increasingly sophisticated mechanisms that reclaim idle cores at microsecond timescales. We argue that this view no longer matches modern server hardware. On contemporary multicore processors, active cores compete for a shared package level power and thermal budget. Once that budget becomes the limiting resource, an idle core that waits efficiently returns compute capacity that hardware can redistribute to productive work. Measurements on a recent AMD EPYC processor show how waiting strategy, processor topology, and idle duration determine this tradeoff. Our results suggest that reclaiming idle cores often yields less benefit than commonly assumed while introducing substantial scheduling complexity. We propose a budget centric view of service core systems in which power, rather than core occupancy, becomes the fundamental resource and waiting policy becomes a first class systems design choice.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[uSTM: A Lightweight and Efficient STM Supporting General Types and Deferred Aborts](https://arxiv.org/abs/2607.18178v1)** | ⭐ 78/100 | 轻量级STM实现，支持通用类型与延迟中止 | 代码极简且性能优异，通过新时间戳算法保证了安全性 | <details><summary>展开</summary>Software Transactional Memory (STM) systems allow developers to more easily exploit multicore architectures by wrapping arbitrary sequential code in transactions that are executed concurrently. In recent years, the performance of STM systems has approached that of hand-tuned data structures through techniques that avoid unnecessary aborts and exploit the semantics of underlying data structures. Despite achieving excellent performance, most STM systems do not fully address the concerns they targeted in the first place: safety, usability, and generality. In particular, these systems place restrictions on the data types that may be updated transactionally, such as requiring that these types fit within a word, and can require modification of data layout. Moreover, most STM systems abort transactions in the middle of client code to ensure correctness. This can cause space leaks and other bugs not present in the original code. We present ustm, a novel STM system addressing all of these shortcomings while still maintaining excellent performance, all within ~300 lines of code. uSTM supports general types while maintaining data layout. Aborts are deferred until the end of the transaction, allowing client code within a transaction to terminate normally. To ensure that uSTM guarantees opacity, we implement a novel timestamping algorithm we call split-increment timestamps. We compare the performance of uSTM to a variety of state-of-the-art (SOTA) STM systems, demonstrating that uSTM matches or outperforms the SOTA on a variety of workloads.</details> |
| **[When to Use Which? Benchmarking Optimisers for Configurable Systems under Varying Budgets](https://arxiv.org/abs/2607.16476v1)** | ⭐ 78/100 | 系统配置调优器在不同预算下的性能基准评估 | 通过大规模实证分析评估了多种调优器，对工程实践有指导意义 | <details><summary>展开</summary>Software configuration tuning is crucial for optimising system performance, and various optimisers have emerged over the last decade. Yet, the time required during the tuning process may vary across systems. In some systems (e.g., PostgreSQL), it may take a few minutes to measure a configuration, whereas in some others (e.g., MariaDB), it can take several hours. Moreover, even within the same system, users may have varying budgets and preferred settings. This naturally raises a question -- Given a budget level, which optimiser is the best choice for SE practitioners? This matters because optimisers usually have their own ``comfort zone'' and may perform very differently under distinct budgets. In this paper, we aim to answer this question. We systematically evaluate eight well-established optimisers across 22 configurable systems under varying budget levels. We find that, unsurprisingly, model-based optimisers (e.g., SMAC) are well-suited under tight budgets, and model-free optimisers (e.g., GAs) become superior with more generous budgets. However, interestingly, there is one optimiser, FLASH, that performs consistently well on most systems regardless of budgets. We lastly investigate the reasons behind this phenomenon and find that many systems possess good local optima (with large basins of attraction), allowing greedy optimisers (e.g., FLASH) to achieve strong performance. Source code, data, and supplementary materials of this work are available at https://anonymous.4open.science/r/Config-W2W-98B2.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Byzantine Fault-Tolerant Post-Quantum Distributed Quorum Signatures](https://arxiv.org/abs/2607.17700v1)** | ⭐ 75/100 | 提出DQS协议解决后量子共识签名扩展性问题 | 通过协议重构实现抗量子共识，工程落地性较强。 | <details><summary>展开</summary>Threshold, aggregate, and multi-signatures -- which we collectively call quorum signatures -- certify that a quorum of nodes endorsed a statement, with a certificate as small as a single signature. No constant-size post-quantum quorum signature is known: all candidates grow with the number of signers and are slow to aggregate, making quorum signatures the hardest obstacle to migrating byzantine fault-tolerant systems to post-quantum security. In this paper, we sidestep this open cryptographic problem by changing how the protocol communicates. We introduce a primitive we call Distributed Quorum Signature (DQS), built solely from ordinary digital signatures and a Bracha-style approval broadcast. DQS turns certificates from network messages into local events. Two event types divide the roles certificates play: weak certificates capture safety, strong certificates capture liveness. In DQS every message is constant size, fitting a single datagram regardless of the number of nodes. The total communication is quadratic, and no security assumptions change. In a large distributed system, the overhead of post-quantum DQS is competitive with the canonical pre-quantum BLS scheme.</details> |


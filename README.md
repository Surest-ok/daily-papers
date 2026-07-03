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

## 2026-07-04

## File Systems & Storage

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[FlintKV: A Fast Durable Storage Engine for Modern Databases](https://arxiv.org/abs/2607.02401v1)** | ⭐ 82/100 | 基于NVM的高性能键值存储引擎 | 针对NVM优化了并发控制与持久化，具备生产级功能。 | <details><summary>展开</summary>Byte-addressable non-volatile memory (NVM) offers an opportunity to rethink storage engine architectures. While recent NVM key-value stores achieve high throughput for ingestion and point lookups, they omit or under-specify the support for the richer interface guarantees required by modern databases. Production key-value engines (e.g., RocksDB) provide point-in-time snapshots, consistent iterators, and atomic batches-features essential for implementing transactions and concurrency control. We present FlintKV, an NVM-optimized skiplist-based storage engine that natively supports the full API of production key-value stores. FlintKV supports both atomic batch writes and snapshot-consistent iteration efficiently while guaranteeing durable linearizability. FlintKV can be deployed standalone or its durable skiplist can be integrated into existing NVM stores to enhance their capabilities. Central to FlintKV is a novel flat-combining based concurrency control algorithm that leverages multi-versioning and carefully co-designed persistence mechanisms to ensure high performance and scalability. Our empirical evaluation shows that FlintKV can achieve up to a 75% improvement in end-to-end throughput over prior work.</details> |
| **[SLFS: a Flexible, Low-Cost Distributed File System Using Serverless Designs](https://arxiv.org/abs/2607.01486v1)** | ⭐ 82/100 | 基于Serverless的弹性分布式文件系统 | 架构创新且评估详实，有效解决了冷启动与成本问题 | <details><summary>展开</summary>Large-scale distributed file systems must provision resources for peak demand, yet file access patterns fluctuate significantly, leaving substantial capacity idle during off-peak periods. Existing scaling mechanisms operate at the granularity of entire servers and take minutes to hours, making them unable to track the rapid, fine-grained load variations that file systems commonly experience. Serverless computing, with its millisecond-granularity elasticity and pay-per-use pricing, offers a compelling alternative. We present SLFS, the first distributed file system built with serverless functions for both data and metadata operations. SLFS implements file services on top of key-value stores, keeping function operations simple and short, and introduces a novel multi-threaded, short-lived server design that overcomes the cold-start problem while maintaining low cost. A policy-enforcing coordinator efficiently maps files to function instances, scales the system elastically, and controls function lifetimes to balance performance and cost. SLFS can flexibly run on diverse storage backends -- from cloud-native services like S3 to user-managed key-value stores -- enabling configurable cost-performance trade-offs. Our evaluation shows that SLFS mitigates cold starts by 580$\times$ compared to the base serverless design and outperforms $λ$FS, EFS, and Ceph at up to 63%, 68%, and 63% lower cost, respectively.</details> |

## Container & Virtualization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware](https://arxiv.org/abs/2607.02357v1)** | ⭐ 78/100 | 提出基于沙箱运行时审计的恶意技能检测系统 | 针对AI代理安全，通过运行时行为分析替代静态扫描，工程实用性强。 | <details><summary>展开</summary>LLM coding agents increasingly rely on third-party agent skills from public marketplaces, which execute with the agent's privileges and create a software supply-chain attack surface: a malicious skill can steal credentials, exfiltrate source code, or install backdoors. Existing defenses use static skill scanners based on pattern matching or LLM-as-judge analysis, but it remains unclear whether they withstand adaptive evasions that preserve malicious behavior while changing payload appearance. This paper first presents an adversarial study of existing skill scanners through SkillCloak, a payload-preserving evasion framework that keeps the attack semantics intact while transforming their visible form. SkillCloak uses two complementary strategies: Structural Obfuscation, which rewrites visible payload indicators into semantically equivalent forms, and Self-Extracting Skill (SFS) Packing, which hides malicious components from the install-time view and restores them during agent execution. Across eight scanners and 1,613 in-the-wild malicious skills, SFS Packing bypasses every scanner at over 90%, while Structural Obfuscation bypasses over 80% on most static scanners and reaches 96% on a hybrid scanner, showing that appearance-based auditing is insufficient. Motivated by this finding, we propose SkillDetonate, a behavior-centric runtime auditor that executes skills in a sandbox and detects malicious effects through OS-boundary information-flow evidence rather than install-time appearance. SkillDetonate combines on-demand closure lift, which observes instructions materialized during execution, with marker-based taint analysis, which tracks sensitive-data flows across the agent context, files, processes, and network operations. The results show that SkillDetonate detects 97% of attacks at a 2% false-positive rate and sustains 87% detection on real-world malicious skills.</details> |

## eBPF & Observability

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[GPUAlert: A Zero-Instrumentation Process-Boundary Monitor for Diagnosing GPU Training-Job Failures](https://arxiv.org/abs/2607.01409v1)** | ⭐ 78/100 | GPU训练任务零侵入故障监控与诊断工具 | 工程实用性强，解决了生产环境监控痛点 | <details><summary>展开</summary>GPU training jobs fail often, roughly two in five on large production clusters, yet the operator typically learns of a failure only by reconnecting hours later. Experiment trackers require editing the training script and maintaining a cloud connection; the scheduler's mail hook delivers a single status line with no cause and no logs. GPUAlert is a command-line wrapper that monitors any training command at the process boundary, and with no change to that command, emails a structured notification on completion carrying a classified failure cause, durable logs, and output artifacts. The tool is organized around three reliability primitives: a pre-launch log guarantee that establishes the durable destination before the child process can crash, notifier isolation that makes the wrapper's exit code a pure function of the child's status regardless of whether the email succeeds, and a non-silent artifact budget that bounds attachment size without ever dropping output silently. We release a labelled corpus of 474 GPU training logs across 15 failure classes and a reproducible evaluation harness. On the twelve hardware-reproduced classes, the ordered-rule classifier reaches 0.997 macro-F1, against 0.830 for unordered keyword matching and 0.133 for exit-code inspection. Wrapper overhead is a constant approximately 3ms per job; the pre-launch guarantee preserves a log where a shell redirect yields nothing; and across all 15 failure modes the wrapper returns the child's exit code unchanged even when the SMTP relay is unreachable.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[AB-Sync: Attention-Based Slot-Level Clock Synchronization Method for UWB-TDOA Localization Networks](https://arxiv.org/abs/2606.28087v1)** | ⭐ 70/100 | 提出基于注意力机制的UWB时隙级时钟同步方法 | 针对UWB定位系统时钟漂移问题，在真实测试平台验证了有效性。 | <details><summary>展开</summary>Ultra-wideband (UWB) time-difference-of-arrival (TDOA) localization networks provide high-update-rate indoor location services for IoT and cyber-physical applications, but their accuracy depends on nanosecond-level clock synchronization among anchors. Existing wireless clock synchronization (WCS) methods typically estimate clock states at the synchronization-stage or interval level, whereas TDMA-based UWB-TDOA systems localize tags from blinks transmitted in discrete short slots inside each synchronization stage. We identify this granularity mismatch as a source of residual TDOA error and present AB-Sync, an attention-based slot-level clock synchronization method. AB-Sync models the relationship between the slot-specific clock-speed ratio required by a target tag blink and neighboring clock-fluctuation observations, thereby enabling tag-slot-level timestamp mapping without adding extra UWB synchronization messages. On a real UWB-TDOA testbed, AB-Sync reduces the multi-anchor average TDOA ranging STD.V by 9.4% and improves representative static localization accuracy by 18.6% compared with Deferred+3S-KF, the leading low-overhead baseline in our evaluation. In a five-slot multi-tag experiment, AB-Sync consistently improves localization stability across all TDMA slots, reducing STD.V by 5.3% on average and up to 16.2% per slot with no extra UWB synchronization overhead.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Kani: A Model Checker for Rust](https://arxiv.org/abs/2607.01504v1)** | ⭐ 88/100 | Rust语言的开源模型检测工具 | 工业级验证工具，已在生产CI中广泛应用 | <details><summary>展开</summary>Rust's ownership type system prevents memory errors in safe code, but certain desirable properties remain orthogonal to compilation: the soundness of unsafe operations (e.g., raw pointer dereferences), functional correctness, and absence of runtime panics. We present Kani, an open-source model checker for Rust that pushes bounded model checking beyond bug-finding to provide correctness guarantees for these properties. Kani compiles proof harnesses from Rust's Mid-level Intermediate Representation (MIR) into CBMC's bit-precise verification engine, automatically checking a comprehensive set of safety properties with no user annotation. To extend verification from bounded to unbounded, Kani provides a specification language comprising function contracts, loop contracts, quantifiers, and function stubbing. We demonstrate feasibility through case studies on industrial Rust projects, where contracts upgraded verification from panic-freedom to functional correctness, uncovering six previously unknown bugs. Kani operates at scale in production CI, with over 16,000 harnesses verified per code change in the Rust standard library verification campaign.</details> |
| **[Elasticity in Parallel Sparse Triangular Solve](https://arxiv.org/abs/2607.02324v1)** | ⭐ 78/100 | 提出弹性并行稀疏三角求解调度器 | 实现了高性能调度器，在多核硬件上验证了显著性能提升。 | <details><summary>展开</summary>We introduce stale synchronous parallel as a mode of execution in parallel sparse triangular linear system solve and present a general directed-acyclic-graph scheduler capable of producing such schedules. Stale-synchronous-parallel schedules allow the overlap of synchronisation and compute which results in a geometric-mean speed-up of $7$-$30\%$ of our scheduler, ElasticDivide, over state-of-the-art synchronous scheduler GrowLocal on an ARM machine using 48 cores. On an x86 machine using 48 cores, we report geometric-mean speed-ups of $19$-$60\%$ over SpMP.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Cadence: Extreme Pipelining with Multiple Concurrent Proposers](https://arxiv.org/abs/2607.02275v1)** | ⭐ 70/100 | 一种支持多提议者的高性能共识协议 | 协议设计创新，但仅限于模拟环境评估，缺乏实机部署。 | <details><summary>展开</summary>We present Cadence, a Byzantine fault-tolerant multi-proposer consensus protocol with arbitrarily low block intervals, optimal resilience, and optimal fast-path latency. Cadence divides time into equally spaced slots, one block per slot, each finalized in its own consensus instance. Blocks do not build directly on their predecessor, so instances run independently and none waits for an earlier block to finish or propagate; we call this extreme pipelining, decoupling the block interval from network latency. Cadence also removes the single-leader monopoly over transaction inclusion and ordering: under multiple concurrent proposers (MCP), several validators propose for each block, and it guarantees that, under synchrony, a transaction a correct proposer includes cannot be censored or deferred (short-term censorship resistance), and that no proposer can craft its proposal in reaction to the others' (hiding). To realize extreme pipelining, we introduce a general framework that turns any one-shot consensus meeting our slot-consensus specification into a multi-shot protocol. We instantiate it for MCP with two protocols of our own: Chorus, a slot consensus whose fast path finalizes a block in an optimal three rounds, with speculative finality one round earlier, and Conductor, an orchestrator that opens slots at an even cadence, more slowly under asynchrony to keep open slots bounded. To our knowledge, Cadence is the first MCP protocol to provide short-term censorship resistance and hiding at the fast-path latency of single-leader consensus. We prove safety, liveness, censorship resistance, and hiding under partial synchrony with optimal resilience (n = 3f+1). In simulation over Monad's 200 validators with five proposers per slot, finalization averages 219 ms (167 ms to speculative finality); at a 100 ms block interval a transaction waits on average 50 ms to enter a proposal.</details> |


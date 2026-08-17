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

## 2026-08-18

## OS Kernel & Scheduling

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[A Bounded Reclaim Actuator for PSI-Guided Compressed Memory: A Controlled Ablation](https://arxiv.org/abs/2608.13689v1)** | ⭐ 78/100 | 基于PSI的受限内存回收机制性能评估 | 通过实机实验对比zram与PSI策略，工程实践价值高 | <details><summary>展开</summary>When the aggregate working set of active processes exceeds physical RAM capacity, the machine experiences memory pressure. Applications may therefore slow down before the kernel kills a process. Linux provides several ways to observe and respond: Pressure Stall Information (PSI) can detect memory-related task stalls, zram can provide compressed in-memory swap space, and cgroup v2 can request memory reclamation within a selected control group. These facilities are often discussed together even though they act at different points in the pressure path. This paper examines that distinction with a controlled systems study. We compare three setups: zram enabled from startup; zram enabled only after PSI indicates memory pressure; and zram enabled from startup with a one-time 96 MiB cgroup reclaim request. We first selected the request size in a 16-case pilot, then ran 180 confirmatory cases, 60 cases for each setup, on nine 1-vCPU Linux virtual machines with compute and SQLite workloads. Compared with static zram, the bounded reclaim configuration reduced compute p99 response time by 6\%, while the SQLite result was statistically indistinguishable. Delayed activation had higher median p99 latency than both alternatives. These results suggest that the benefit depends on the foreground workload and its memory-access path, rather than a general improvement across workloads.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Weird Machines in Transport Layer Security](https://arxiv.org/abs/2608.13685v1)** | ⭐ 78/100 | 揭示TLS握手协议中的图灵完备计算能力与安全隐患 | 通过实证分析TLS协议逻辑漏洞，具备极高工程价值 | <details><summary>展开</summary>Weird machines are latent computational capabilities that emerge from the composition of architectural components. Prior work has studied this phenomenon extensively in software systems, including x86 instructions, ELF metadata, and page tables, and more recently in cyber-physical systems such as industrial control networks. This paper extends weird machine theory to a new domain: the Transport Layer Security (TLS) handshake and its two dominant implementations, OpenSSL and BoringSSL. We show that legitimate TLS primitives, including session cache entries, renegotiation logic, extension parsing, and certificate verification steps, compose into Turing-complete systems whose computation is coupled to authentication and trust decisions rather than physical actuation. We formalize this coupling, which we call trust actuation, and argue that any TLS implementation providing session storage, arithmetic on sequence counters, conditional branching on handshake state, and iteration through resumption or retry loops satisfies the conditions for arbitrary computation. We validate this theory with two working demonstrations built on real OpenSSL code paths. The first, a sentinel system, composes standard TLS primitives into a defensive mechanism that detects anomalous handshake behavior. The second, an authentication bypass, composes the same class of primitives into an attack that defeats a cipher-strength policy check through mid-connection renegotiation, without any memory corruption or external malware. Both demonstrations run against real server and client binaries in Docker.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Balancing Workload Performance and Slurm Stress: Four Nextflow Deployment Strategies](https://arxiv.org/abs/2608.13824v1)** | ⭐ 82/100 | 评估四种Nextflow在Slurm集群上的部署策略 | 在生产集群上进行了实测，方法论严谨且具备实用价值 | <details><summary>展开</summary>Wide Nextflow fan-outs on shared Slurm clusters can submit tens of thousands of short tasks. Deployment choices - individual jobs, arrays, or nested schedulers within allocations - affect both workflow turnaround and RPC volume, a shared cost that can degrade scheduler responsiveness. Existing studies compare whole workflow systems, while per-task queueing metrics do not span architectures that dispatch inside an existing allocation. We present a reproducible measurement protocol and bench harness with two key elements. First, a clean-start clock begins before any backend service or allocation request, placing different architectures on a common time axis. Second, per-user Slurm sdiag counters measure attributable RPC demand, with controller processing time reported as a sensitivity context separate from cluster-wide state. We evaluate four multi-node strategies: Slurm native, Slurm job arrays, HyperQueue, and Flux, on the shared ASU Phoenix production cluster; the single-user Dev campaign includes native, arrays, and Flux. The fixed workload contains 4,823 LASTZ tasks, with one clean-start trial per configuration in this preliminary campaign. Results show a walltime-RPC trade-off. On Phoenix, arrays and HyperQueue reached the milestone in 0.32 h, while Flux took 0.65 h but reduced attributable RPCs to 1,396 per 1,000 terminal tasks; all three were non-dominated. On Dev, arrays and Flux formed the observed frontier: 0.80 h for arrays versus 0.84 h for Flux, with Flux reducing RPCs to 1,769 per 1,000 terminal tasks. The method enables HPC sites to compare deployment strategies using metrics that capture both user experience and scheduler impact, and to choose the fastest strategy within a site-specific RPC budget.</details> |


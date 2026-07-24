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

## 2026-07-25

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[STORM: RDMA-based Monte Carlo Transport Scheme for Distributed-Memory Particle Simulations](https://arxiv.org/abs/2607.20639v1)** | ⭐ 88/100 | 基于RDMA的分布式粒子传输通信库 | 利用RDMA实现高性能通信，实测扩展性极佳且开源 | <details><summary>展开</summary>Monte Carlo particle transport enables high-fidelity astrophysical radiation and neutrino simulations - from core-collapse supernovae and neutron-star mergers to accretion flows - by handling multidimensional geometries, frequency dependence, and moving media without angular discretization. However, inter-rank communication limits scalability on unstructured meshes: standard two-sided MPI requires receivers to post receives and poll completions, creating per-iteration progress overhead that grows with the number of communication partners. Such problems have not demonstrated high scaling efficiency at $O(10^4)$ cores. We present STORM (Scalable Transport via One-sided Remote Memory), an open-source library for Monte Carlo transport on general meshes, physics, and boundary conditions. STORM provides a lock-free, mesh-independent communication layer that replaces MPI's matched-send/receive semantics with Remote Direct Memory Access (RDMA) - one-sided operations that write directly into a remote rank's memory without involving its CPU. Each rank pair shares a single-producer, single-consumer ring buffer; RDMA writes transfer particles while receivers remain passive. A two-sided MPI backend provides a portable fallback. In an adversarial uniform-emission benchmark, the RDMA backend sustains $&gt;97\%$ weak-scaling and $&gt;88\%$ strong-scaling efficiency up to 13,440~cores (112~cores per network adapter), with $1.14$-$1.27\times$ speedups over the two-sided alternative. In a Hohlraum IMC benchmark at 4480 ranks, it is $1.41\times$ faster because MPI progress overhead is reduced by $6.1\times$. By decoupling communication from physics models and mesh representations, STORM removes a barrier to scaling Monte Carlo transport in astrophysical multiphysics codes, enabling coupled radiation-hydrodynamics with energy- and angle-resolved photon or neutrino transport on dynamically evolving meshes at scale.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[DMG: A Scalable and Efficient Memory-Disaggregated Graph Processing System](https://arxiv.org/abs/2607.20881v1)** | ⭐ 82/100 | 一种可扩展且高效的内存解耦图处理系统 | 解决了内存解耦架构下的扩展性与缓存效率问题，实验扎实且具有工程实用价值。 | <details><summary>展开</summary>Traditional graph processing systems are built on monolithic servers, which couple a fixed ratio of compute and memory resources but often result in resource under-utilization in data centers. Although the disaggregated memory (DM) architecture has emerged to address this inefficiency, we identify that existing graph processing systems on DM remain highly impractical. They rely on unscalable architectures that fail to scale beyond a single memory node and a single compute node, and they require compute-side caches that are orders of magnitude larger than conventional practice in DM. To this end, this paper presents DMG, the first practical graph processing system on DM, which demonstrates superior system scalability and cache efficiency while delivering high performance. To improve efficiency of graph retrieval on DM, DMG proposes a DM-friendly graph store with retrieval optimizations. To mitigate costly update propagation, DMG presents an adaptive update coordinator that coordinates compute and memory nodes to perform update propagation with low overhead. To enable fast and effective load balancing, DMG employs a two-stage workload manager that includes a coarse-grained initial partitioning and a fine-grained runtime re-scheduling. Experimental results substantiate that compared with the state-of-the-art DM-based graph processing system, DMG can elastically scale up both compute and memory resources, delivering up to 4.9X better performance and accommodating graphs with ever-increasing sizes; meanwhile, it effectively tames the compute-side cache demands by up to 18.9X, positioning itself as a DM-ready solution in practice.</details> |
| **[Multimmit: Extending Blocks for Faster Finality](https://arxiv.org/abs/2607.21021v1)** | ⭐ 70/100 | 提出多链数据分发协议以提升共识效率 | 分布式共识协议创新，但缺乏大规模生产部署验证 | <details><summary>展开</summary>To meet the throughput demands of modern blockchain systems, protocols for State Machine Replication (SMR) increasingly have many processors disseminate blocks of transactions in parallel, with consensus then establishing a total ordering on the blocks of all producers. Such designs face a choice as to when a block may enter the ordering. Certified approaches wait for a quorum to attest a block's availability, which is robust but adds message delays to every transaction. Uncertified approaches let proposals reference blocks immediately, which is fast but degrades rapidly when referenced data must be fetched on the critical path. Raptr, the state of the art, takes a middle course, finalising the longest prefix of the leader's proposal that a quorum holds, so that no processor ever blocks or fetches. The remaining weakness is sensitivity to order: if the data behind a single early batch is withheld, the proposal finalises little or nothing, so individual faulty producers can still deny the system its optimistic path. We present Multimmit, a protocol for $n \ge 5f+1$ processors combining a consensus layer requiring one round of voting per view with multi-chain data dissemination. Votes are cast relative to the leader's proposal, reporting per chain how far the voter can support it, and may themselves attest fresh blocks beyond it. A transaction block disseminated at time $t$ is ordered by $t+3δ$ in expectation and $t+2δ$ at best, measured from the block's dissemination rather than the leader's proposal. Degradation under faults is graceful: a faulty producer delays only its own chain's blocks, costing other chains at most a one-view wait for placement. No leader can both finalise its leader block and exclude a fresh, well-circulated block of an honest chain. Consensus traffic is tens of kilobytes per view, independent of transaction volume.</details> |


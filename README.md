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

## 2026-07-10

## Container & Virtualization

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Seekable OCI: Lazy-Loading Container Images via Range-Request Indexing](https://arxiv.org/abs/2607.06868v1)** | ⭐ 93/100 | 通过索引实现OCI镜像按需加载，大幅提升容器启动速度 | 生产环境大规模部署，性能提升显著，工程价值极高 | <details><summary>展开</summary>Container image pulling accounts for the majority of pod startup time in Kubernetes environments. Standard pull downloads the entire image before the container can start, even when the application accesses only a fraction of the image content at startup. We present SOCI (Seekable OCI), a lazy-loading architecture that enables containers to start without downloading the full image. SOCI builds an external index over standard OCI images, mapping files to byte ranges within compressed layers. At runtime, a FUSE filesystem intercepts file accesses and serves them via HTTP range requests. Unlike prior approaches that require image format conversion, SOCI works with unmodified images and standard registries. The index is stored as an OCI referrer artifact, requiring no changes to images, registries, or deployment tooling. On a 1.3 GB Python web service image, SOCI reduces cold-start pull time from 20 seconds to approximately 2.8 seconds (7.4x speedup), with pull time independent of image size. Larger images see larger speedups (9.3x on a 2.5 GB image) because SOCI pull time is constant while standard pull scales linearly. We measure a crossover at 80% access density: below this, lazy loading wins; above, parallel full pull is faster. SOCI lazy loading is deployed in production on Amazon EKS and Amazon ECS Fargate (which launched 18.4 million tasks per day during Prime Day 2025), and has been serving lazy-load requests since 2023. EKS Auto Mode uses SOCI's parallel pull mode for GPU instances.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Unveiling TCP BBR Dominance in Starlink Internet: Experimental Insights and Analysis](https://arxiv.org/abs/2607.07133v1)** | ⭐ 82/100 | 评估BBRv3在星链网络中的拥塞控制性能 | 基于全球真实测试床的实测分析，工程参考价值高 | <details><summary>展开</summary>This experimental study delivers a global assessment of Google's Bottleneck Bandwidth and Round-trip propagation time-version 3 (BBR-v3) Congestion Control Algorithm (CCA) over SpaceX's Starlink network. Leveraging a strategically deployed six-city testbed across five continents, we systematically benchmark BBR-v3 against eight CCAs: Cubic, Hybla, Vegas, LeoCC, Copa, PCC, BBR-v1, and BBR-v2 under both dedicated and concurrent conditions. Our results demonstrate that BBR-v3's advantage is not aggressive bandwidth capture, but a more balanced fairness, loss, and delay trade-off over the Starlink Internet. We develop pragmatic mathematical models that capture Starlink's complex network dynamics and characterize BBR-v3 behavior to better explain the experimental observations. Our extensive evaluation of queue buildup and fairness further demonstrates BBR-v3's capability to maximize throughput in high-latency, variable satellite environments, while maintaining a balance between aggressiveness and fairness. The findings establish BBR-v3 as a compelling CCA for Low Earth Orbit (LEO) satellite networks and provide a principled analytical foundation for next generation satellite Internet transport design.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Finding and Understanding Miscompilation Bugs in the Solidity Compiler](https://arxiv.org/abs/2607.07217v1)** | ⭐ 75/100 | 提出SolSmith工具以发现Solidity编译器漏洞 | 通过差分模糊测试有效提升了关键基础设施的编译器安全性 | <details><summary>展开</summary>Smart contract compilers are critical to ensuring the correctness of public blockchains whose defining characteristics are open-source and immutable code. We created SolSmith, a semantics-aware differential fuzz testing tool, to improve the quality of the Solidity compiler -- the most popular compiler for the Ethereum blockchain -- and spent over three years finding compiler defects that produce incorrect code. We call these defects miscompilation bugs. During this time period, we have discovered 25 miscompilation bugs that went unnoticed, some for multiple years. Our first contribution is to make compiler testing more rigorous. SolSmith achieves this goal by generating valid test programs that are likely to stress test code generation and optimization components. This helps SolSmith find bugs missed during routine testing that could potentially have serious implications for smart contracts and their users. Our second contribution is a qualitative and quantitative analysis of miscompilation bugs that we found in the Solidity compiler. We classify miscompilation bugs found by SolSmith based on their nature, root-causes, and impact on end-users. This sheds light on some pitfalls of optimizing compilers.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Scaling WaterLily.jl with MPI and an improved geometric multigrid solver](https://arxiv.org/abs/2607.07687v1)** | ⭐ 75/100 | 通过MPI与多重网格优化提升流体求解器性能 | 工程实现扎实，并行扩展性测试详尽，符合系统工程范畴 | <details><summary>展开</summary>We present recent performance-oriented developments in WaterLily.jl, a scale-resolving incompressible flow solver written in pure Julia that runs seamlessly on CPUs and GPUs of any vendor. Supported by the newly added MPI-based parallelism, strong-scalability tests display a near-ideal linear trend, and weak-scaling efficiency is kept above 85\% before node memory-concurrency contention dominates parallel performance. Inter-node weak scalability is sustained above 96\% with grid size up to 1 billion cells. We further benchmark improvements to the geometric multigrid Poisson solver enabled by an adaptive under-relaxed red-black Gauss--Seidel smoother together with anisotropic coarsening operators.</details> |


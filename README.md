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

## 2026-06-09

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[i2Slicer: Enabling Flexible and Automated Orchestration of 5G SA End-to-End Network Slices](https://arxiv.org/abs/2606.06955v1)** | ⭐ 78/100 | 提出i2Slicer实现5G端到端切片自动化编排 | 系统实现完整且在真实5G软硬件环境下进行了有效评估 | <details><summary>展开</summary>5G network slicing implies a step forward in customizing radio access and core networks by allowing the creation of logical networks adapted to service requirements. In addition, softwarisation has fueled the emergence of 5G solutions which do not require specialized hardware platforms. Therefore, a key requirement to drive the adoption of 5G slicing by verticals is to simplify its management through automated orchestration. In this paper, we present i2Slicer, a flexible solution to orchestrate the deployment of 5G standalone end-to-end network slices with multi-tenancy and multi-service capabilities. The implementation and evaluation of i2Slicer using state-of-the-art 5G software and hardware demonstrate that it offers a practical and efficient lifecycle management of network slices.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[AgileOS: A GPU Operating System Layer for Protected CUDA Services](https://arxiv.org/abs/2606.06697v1)** | ⭐ 78/100 | 实现CUDA服务隔离的GPU操作系统层 | 通过PTX注入实现GPU内存隔离，架构设计实用 | <details><summary>展开</summary>Modern GPU applications increasingly interact with storage systems, network devices, vendor libraries, and GPU-resident services rather than executing only isolated compute kernels. This shift creates a need for operating-system-like protection around GPU services, where service metadata, device queues, memory-mapped I/O regions, and library-internal state should not be directly exposed to untrusted application kernels. However, today's CUDA programming model, by default, still gives each application direct ownership of its CUDA context, device pointers, runtime handles, module loading path, and kernel launches, leaving protected GPU services to build their own ad hoc interfaces and isolation mechanisms. This paper presents the initial design and prototype scope of AgileOS, a GPU operating-system layer for protected CUDA services. AgileOS virtualizes CUDA at the library boundary: applications link against client-side CUDA Runtime, Driver, and selected library shims, while a trusted runtime worker owns the real CUDA context and mediates supported operations. To protect service state and module interfaces, AgileOS also defines a GPU memory-management model that separates user allocations from protected module/MMIO ranges, using pointer validation and memory access guards via PTX injection. AgileOS is modularized and flexible, supporting a range of protected services and existing libraries such as cuFFT and PyTorch. The prototype includes client-side interceptors, worker-side CUDA handlers, virtualized CUDA object tables, protected AgileOS modules, a GPU memory manager that separates user allocations from protected module/MMIO ranges, selected trusted library adapters, and the PTX-level kernel memory guard.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Communication Strategy Selection for Multi-GPU 3D FDTD with Convolutional Perfectly Matched Boundary Layers](https://arxiv.org/abs/2606.06910v1)** | ⭐ 75/100 | 多GPU下FDTD通信策略优化研究 | 针对GPU通信瓶颈的工程优化，评估详实且具有实用价值。 | <details><summary>展开</summary>In this paper we describe a communication-strategy study for multi-GPU three-dimensional finite-difference time-domain computation with convolutional perfectly matched layer boundary conditions using CUDA. The metrics used to determine the most effective implementation include runtime, throughput in millions of output points per second, strong-scaling efficiency, CPML overhead, host-staged versus direct GPU-to-GPU exchange speedup, and enlarged-ghost speedup. On a single NVIDIA Quadro RTX 6000 GPU, the CPML implementation sustains 2,889--3,290 million output points per second with less than 1\% boundary-layer overhead, providing the single-GPU baseline for the multi-GPU study. The results show that direct GPU-to-GPU peer exchange is the dominant optimization with a 2.46--2.76$\times$ speedup over host-staged exchange, while enlarged ghost regions give only modest benefits because the reduced communication frequency is partly offset by redundant computation and additional memory traffic. On NVIDIA Quadro RTX 8000 GPUs, the implementation gives up to a 1.51$\times$ speedup on two GPUs for the tested strong-scaling cases, while four GPUs enable larger grids that approach or exceed single-GPU memory capacity.</details> |


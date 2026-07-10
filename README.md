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

## 2026-07-11

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Toward a Unified GPU-Aware OpenSHMEM Specification](https://arxiv.org/abs/2607.08006v1)** | ⭐ 75/100 | 提出OpenSHMEM GPU感知通信规范以提升跨平台兼容性 | 针对HPC通信标准化的工程实践，具备良好的实用性与明确的规范定义。 | <details><summary>展开</summary>Leadership-class HPC systems are now accelerator-centric, with GPUs providing most floating-point throughput and memory bandwidth. As next-generation systems increasingly integrate accelerators through high-speed memory fabrics and system interconnects, exposing larger tightly coupled device domains, \ac{PGAS} models such as OpenSHMEM provide a natural abstraction for expressing fine-grained remote memory operations across these devices. While OpenSHMEM 1.x offers a lean PGAS model for irregular communication, atomics, fine-grained synchronization, and collectives, its memory model lacks portable semantics for accelerator architectures. As a result, existing GPU-enabled OpenSHMEM implementations differ in memory management, capability discovery, and operation semantics, limiting portability and ecosystem cohesion. This risks fracturing the community that OpenSHMEM was originally created to unify. This paper proposes an OpenSHMEM Auxiliary Specification for GPU-Aware Communication, designed as a lightweight, backward-compatible extension to OpenSHMEM 1.x. The auxiliary specification introduces a minimal memory model extension via a GPU-scoped memory space abstraction, along with capability queries and well-defined semantics for using \acs{GPU}-attached buffers in RMA, atomic, synchronization, and collective operations. This is initially conceived through the lens of a host-initiated interface, although it provides a general set of semantics that also allow for optional device-initiated support. A central goal of this effort is to demonstrate that GPU-aware OpenSHMEM semantics can be specified and implemented across GPUs from multiple vendors, providing a practical and rapidly implementable step toward unification under a vendor-neutral specification while informing the design of future OpenSHMEM specifications.</details> |


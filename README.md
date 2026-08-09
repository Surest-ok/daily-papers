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

## 2026-08-10

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[PortLBM: A Portable Lattice Boltzmann Tool Leveraging SYCL on AMD, NVIDIA, and Intel GPUs](https://arxiv.org/abs/2607.20650v1)** | ⭐ 70/100 | 基于SYCL的跨平台流体仿真框架 | 实现了跨GPU架构的LBM仿真，工程实用性较强 | <details><summary>展开</summary>The lattice Boltzmann method (LBM) is a well-established approach for simulating fluid flows at the mesoscopic scale. With the stagnation of Moore's law, high-performance computing has shifted toward GPU accelerators, necessitating programming models that ensure both portability and efficiency across diverse hardware platforms. We present PortLBM, an extensible portable LBM framework built on SYCL that integrates cross-platform GPU support with interactive real-time visualization. PortLBM supports diverse simulation scenarios ranging from Kármán vortex streets and wing flows to porous media, and is designed for easy extension with new algorithms and backends. As part of a performance portability study, we evaluate PortLBM on contemporary GPU architectures from NVIDIA, AMD, and Intel, examining the impact of three data layouts (stream, bundle, and collision) and four algorithmic variants on simulation throughput. Our results show that no single configuration achieves optimal performance across all GPU vendors, confirming the need for system-specific tuning. The stream layout maximizes bandwidth and performs best on the contemporary NVIDIA and Intel GPUs, while the bundle layout improves cache efficiency and excels on the AMD GPU. Two-lattice schemes achieve higher throughput while one-lattice schemes are preferable under memory constraints. Our work underscores the necessity for adaptable, portable LBM software in increasingly heterogeneous computing environments.</details> |


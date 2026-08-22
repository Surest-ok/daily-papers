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

## 2026-08-23

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Concurrency Response of Plain Global Loads on the NVIDIA H100](https://arxiv.org/abs/2608.15764v1)** | ⭐ 75/100 | 揭示H100 GPU全局加载并发性能下降机制 | 通过微基准测试深入分析GPU内存架构性能瓶颈 | <details><summary>展开</summary>The bandwidth a memory-bound GPU kernel sustains is set by how many bytes it keeps in flight. We use Little's Law here as throughput accounting, not as a measured hardware pool. CUDA fills that budget on Hopper through plain loads (ld.global) and asynchronous copies (cp.async), among other paths; we characterize their concurrency response with clean-room microbenchmarks on three H100 SXM5 dies. Our main result concerns the plain-load path: attained LDG bandwidth peaks at a small offered per-thread load (K ~ 2) and then declines, by about 35% from K=2 to K=8 at our primary configuration. The decline survives a fixed-work control matching total issued logical loads across K, ascending and reversed sweep orders, and replication on two dies with the same instrument (-35.0% and -35.2%). Separately profiled counters show DRAM bytes nearly constant over K=2-&gt;8 while L2-sector traffic rises, and a 40x nominal allocation-size sweep (512 MB to 20 GB, all above the ~50 MB L2; no address trace) leaves the decline essentially unchanged, disfavoring a simple allocation-size dependence. Because the L2 hit-rate nonetheless rises with K at every allocation, the aggregate request stream does change with K; we report K as offered software ILP and leave the hardware mechanism open. A preliminary survey adds a matched cp.async-versus-plain-load comparison (2.1-2.9x at high offered depth, two dies), a die-B same-CTA two-stream observation whose companion die-C check differs and is not pooled, and a cross-die primitive baseline.</details> |


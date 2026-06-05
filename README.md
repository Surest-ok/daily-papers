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

## 2026-06-05

## eBPF & Observability

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[UModel: An Agent-Ready Observability Data Modeling Method at Scale](https://arxiv.org/abs/2606.04799v1)** | ⭐ 78/100 | 构建对象中心化可观测性建模框架 | 在阿里生产环境落地，具备高可用与高性能，实用性强 | <details><summary>展开</summary>When networked system failures occur, automatically performing Root Cause Analysis (RCA) using observability data is critical for ensuring networked system reliability. Recently, LLM-based agents have shown promise for automating this diagnosis process through advanced reasoning and autonomous exploration. However, existing observability frameworks remain archaic, characterized by fragmented data silos, incompatible schemas, and insufficient semantic metadata, preventing agents from establishing the complex relationships required for effective RCA. To address these challenges, we present UModel, a unified ontological framework that shifts observability from data-centric to object-centric modeling. UModel constructs a virtual ontological layer where heterogeneous telemetry, entities, and expert knowledge are standardized as objects and interconnected via semantic graphs. In addition, we introduce U-SPL, a pipeline-based query interface that enables agents to autonomously explore system topologies and correlate multimodal data. By re-modeling the "AIOps 2025 Challenge" dataset using UModel, the precision of root cause localization improved by 8%, demonstrating that enhanced data organization can significantly increase the accuracy of downstream tasks. UModel provides a scalable modeling framework that, in its deployment at Alibaba Cloud for more than one year, has served tens of thousands of users, sustained millions of operations per second, and delivered sub-second query latency.</details> |


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

## 2026-06-29

## File Systems & Storage

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[StorRep: Storage Research Experiment Patterns on Chameleon Cloud and Trovi](https://arxiv.org/abs/2606.16252v1)** | ⭐ 75/100 | 提供存储实验的可复现性模式与基准框架 | 提升了存储研究的复现性，具有良好的工程实践价值 | <details><summary>展开</summary>Storage experiments are vital to advancing storage research, but creating extensible and reproducible storage artifacts can be a challenging task. Our research has shown that only 1% of SSD simulator-based experiences are packaged and 0.5% of them can be easily reproduced. The lack of such artifacts without proper reproducibility can significantly impede the advancement of storage research. The biggest challenges in these types of experiments are ensuring that we have the correct environment to conduct them and creating extensible experiments that can be built upon in future research. To address this issue, we introduce StorRep, a thorough study that provides six extensible and reproducible storage experiment artifacts that serve as the foundation for further storage research, utilizing the Chameleon infrastructure. Our study offers experiment patterns and guidelines that can help researchers create transparent and dependable storage experiments. We have successfully integrated our methods in several experiments in multiple community and educational events over several years and produced publicly accessible artifacts that can be extended and fully reproduced without any restrictions.</details> |


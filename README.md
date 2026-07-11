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

## 2026-07-12

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[On the Correctness of Software Merge](https://arxiv.org/abs/2607.07987v1)** | ⭐ 78/100 | 提出基于范畴论的结构化代码合并工具 | 通过语法标准提升合并正确性，实验评估详实且具有工程价值。 | <details><summary>展开</summary>Three-way merge tools play crucial roles in modern software development, where a developer forks a branch to make local modifications and requests it to be merged into the main branch via a "pull request." Despite its importance, the task has traditionally been defined in an intuitive manner, and the results of merge tools are often accepted without scrutiny. In this paper, we present a new structural merge tool in comparison with existing tools based on the syntactic criteria we propose for evaluating the merge results. We require the merge result to be both parsable and universal. Being parsable means that the result is syntactically valid according to the grammar of the programming language. Being universal means that the result incorporates all and only the edit operations occurring in each branch while ensuring that edits common to both branches are applied only once. This requirement can be precisely defined using the notion of pushouts in category theory. In a large-scale experiment involving 43,774 file merge scenarios from 76 open-source Java projects, we found a number of incorrect results reported by existing tools such as the Git companion merge tool, whereas our tool reports none. We further compared d3j's results with 2,582 developer-resolved merges and with 2,459 merge scenarios involving 21 refactoring types. These experiments revealed both the strengths and current limitations of structural merge, and underscore the importance of clear correctness criteria. We expect that the proposed criterion will provide a foundation for developing more reliable and principled merge tools.</details> |


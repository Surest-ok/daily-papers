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

## 2026-08-30

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[FaultLens: Learning Compact Behavioral Test Suites for Generated Operational Programs](https://arxiv.org/abs/2608.26746v1)** | ⭐ 75/100 | 一种用于生成式程序的高效测试套件生成方法 | 通过贪婪算法与多样性策略优化测试集，具备实际工程价值 | <details><summary>展开</summary>Generated operational programs are often validated with either a few hand-written examples or exhaustive regression suites. The former can miss sparse boundary and interaction faults, while the latter can be unnecessarily expensive. We introduce FaultLens, a method for learning compact behavioral test suites while preserving an auditable connection to executed evidence. It executes a rich probe domain once, stores the fault-probe kill relation as a sparse outcome cache, and learns probe orderings only from earlier program generations. A fault-driven greedy component exploits known kill structure, while a mutation-independent diversity component covers probe families, cases, templates, and temporal bins. Their alternating hybrid remains useful when a new program contains a fault mechanism absent from ordering construction. We evaluate twenty generated operational policies across four environments, ten execution seeds, 1,200 measured run summaries, 2,160 controlled program transformations, and 4,120,200 executed program-probe pairs. Of 1,960 intended faulty transformations, 1,779 alter a contract or output somewhere in the finite audit domain; 200 additional controls preserve behavior. A 32-probe hybrid learned on generations 1-3 covers 576/582 (99.0%) dynamically killable faults in generations 4-5 using 1.2-2.0% of the exhaustive domain. With an entire fault family withheld from training, diversity raises scenario-family macro coverage from 84.6% to 94.9%. In a downstream deployment study, a conservative admission rule reduces severe tail regressions from 15/20 program-environment groups to 0/20. FaultLens provides a prioritized evidence mechanism, not a proof of correctness, and makes its budget, evidence source, generalization split, and misses explicit.</details> |


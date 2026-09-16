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

## 2026-09-17

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[TasmScan: Continuation-Aware Taint Analysis for TVM Bytecode with Savelist Abstraction](https://arxiv.org/abs/2609.16987v1)** | ⭐ 78/100 | 针对TON虚拟机字节码的污点分析框架 | 针对TVM字节码的静态分析，实用性强且评估充分 | <details><summary>展开</summary>The Open Network (TON), with a peak market capitalization exceeding $20 billion and over 175 million activated on-chain addresses, relies on the TVM (TON Virtual Machine) to execute smart contracts. TVM uses first-class continuations with savelists to manage control flow and register state across continuation invocations. Since savelist-captured registers allow data to flow across continuation boundaries without passing through the operand stack, bytecode-level analyses cannot construct complete data flow tracking without explicitly modeling savelist semantics. We present TasmScan, the first bytecode-level static analysis framework for TVM that enables cross-continuation data flow reasoning without requiring source code. TasmScan models savelist semantics via forward register analysis with a formal over-approximation guarantee for exact-resolved save sites and locally tracked register definitions, then lifts bytecode into TASIR, a typed intermediate representation, and performs path-sensitive taint analysis with context-aware sources to detect defects. We evaluate TasmScan on 2,921 contracts from the TON verifier registry and a labeled benchmark of 208 contracts with human-confirmed ground truth. On the full corpus, TasmScan resolves 294,546 dynamic continuation targets with 100% precision; ablation confirms that savelist propagation is essential for resolving indirect register calls that depend on cross-continuation register passing. On the benchmark, TasmScan detects 95.3% of defects across five classes with 96.8% precision. A 366-pair stratified sample from the full corpus estimates 85.8% overall precision. TasmScan offers a 17x median speedup over the state-of-the-art symbolic-execution baseline, and in the path-analysis comparison completes 100% of analyses with zero crashes or timeouts.</details> |


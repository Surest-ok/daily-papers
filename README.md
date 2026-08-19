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

## 2026-08-20

## Cloud Native Infrastructure

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[LoRIS: LoRaWAN-based IoT Platform for Sustainability Monitoring in Hotels](https://arxiv.org/abs/2608.17467v1)** | ⭐ 78/100 | 基于LoRaWAN的酒店可持续监测IoT平台 | 大规模生产环境部署，工程实践扎实，实用性强。 | <details><summary>展开</summary>The hospitality sector is a major source of global greenhouse gas emissions, water stress, and waste generation, yet sustainability reporting in hotels remains constrained by coarse, manually collected operational data. We present LoRIS (LoRaWAN-based IoT platform for sustainability monitoring in hotels), a LoRaWAN-based sensing system that delivers high-resolution measurements of resource consumption, environmental conditions, and guest behaviour across geographically distributed hotel properties. The architecture follows the canonical LoRaWAN reference model and is built for the operational realities of hospitality deployments: restrictive hotel IT policies, guest privacy expectations, rapid and reversible installation, and multi-year battery operation. Privacy-by-design guides modality selection and deployment zoning, and end-to-end encryption protects data from sensor to dashboard. This system has been running since February 2022 and currently spans 850 sensors of 19 types across 21 sites in Australia and Slovenia, covering both the AU915 and EU868 regulatory regions. The platform has generated over 202 million sensor records and ingests approximately 245,000 uplink messages per day on managed serverless infrastructure. Our system has been successfully used for seven field studies spanning food waste, energy consumption, and water consumption, including controlled intervention experiments that measure environmental outcomes and guest satisfaction in parallel. This system shows that LoRaWAN sensing can be deployed at scale in operational hotels without compromising guest experience or privacy.</details> |

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Unified Message Model for Heterogeneous Serial Data Exchange Protocols](https://arxiv.org/abs/2608.17642v1)** | ⭐ 70/100 | 提出一种用于异构串行数据交换的统一消息模型与工具链 | 针对嵌入式通信协议的工程化建模，具有较强的工业实用价值 | <details><summary>展开</summary>Modern embedded systems are becoming increasingly complex and typically integrate numerous heterogeneous devices, such as controllers, sensors, actuators, and supporting subsystems. As a result, their development and integration involve a wide variety of serial communication protocols, ranging from standardized solutions to partially standardized and fully project-defined formats. Efficient development of such systems increasingly depends on automation toolchains, which in turn require a clear, unified, and machine-processable formal basis. This paper proposes a unified, protocol-agnostic message model for explicit and deterministic description of serial messages. The model is based on formal definition of data types, atomic message elements (containers), and complete message structure. In addition to the model itself, the paper introduces methods for practical work with it, including configurable message types for expressing structural constraints and supporting deterministic automation, as well as configurable user representations for engineering-oriented reading and editing. The proposed model and methods are demonstrated through implementation in an industrial tool environment. The results show that the approach can support machine-readable interface control document development, automated generation of transport-layer software, and practical engineering work with both standardized and weakly formalized serial protocols. Taken together, the proposed model, methods, and tool implementation provide a practical foundation for automation toolchains in heterogeneous serial communication development.</details> |

## Middleware & Runtime

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[The Polyglot's Dilemma: Conformance Testing a Dozen Specs in as Many Languages](https://arxiv.org/abs/2608.18039v1)** | ⭐ 78/100 | 通过统一YAML测试框架实现多语言驱动的一致性验证 | 工业界大规模实践，有效降低了多语言维护的工程复杂度 | <details><summary>展开</summary>MongoDB maintains client libraries in a dozen programming languages, used by tens of thousands of organizations and millions of developers. Most are implemented natively rather than as wrappers around a shared core. Ensuring consistent behavior across these libraries, comprising millions of lines of code, is hard but essential. Over eleven years, we developed a specification-based testing approach: tests are written once in YAML and executed by language-specific interpreters for each library. We describe the evolution from many ad-hoc formats to a Unified Test Format, which allowed us to delete over 22,000 lines of test code. The rate of nonconformance bugs fell up to 86% in drivers that adopted YAML tests (though results varied). We report lessons learned about declarative test design, test architecture, schema evolution, and the limits of unification.</details> |
| **[COMMITGUARD: Differential Slice Fuzzing for Commit-Induced Bug Detection](https://arxiv.org/abs/2608.17401v1)** | ⭐ 78/100 | 基于差分切片模糊测试的提交级漏洞检测系统 | 针对代码变更的实用测试工具，评估扎实且有效。 | <details><summary>展开</summary>Modern software systems evolve through frequent commits that implement bug fixes, features, and security patches. Although code review and testing are widely used to check these changes, they often provide limited assurance for memory-safety issues. Code reviewers may miss subtle boundary, lifetime, or initialization errors, while existing tests may not exercise the specific paths affected by a commit. Fuzzing is effective at exposing such bugs, but applying it to every commit remains impractical because whole-program fuzzing is expensive, requires suitable harnesses, and may still fail to reach the code changed by a commit. In this paper, we introduce COMMITGUARD, a commit-aware differential slice-based fuzzing approach for verifying code changes. The key insight behind COMMITGUARD is that the pre-commit version of a modified function can serve as a behavioral baseline for interpreting bugs found after the commit. For each target commit, COMMITGUARD identifies modified functions, extracts compilable code slices from both the pre-commit and post-commit versions, and fuzzes the paired slices independently. It then compares sanitizer reports across the two versions and reports bugs that emerge only in the post-commit version as candidate commit-induced bugs. We evaluate COMMITGUARD on 300 commits from openSSL, libpcap and leptonica. Slice fuzzing initially produces 518 sanitizer reports across these commits. By comparing pre-commit and post-commit slices, COMMITGUARD narrows this large output to 7 candidate commit-induced bug reports that require manual triage. Manual validation confirms 5 of these reports as real bugs that were fixed by developers of the examined projects after we reported them, while only 2 reports were classified as false positives. COMMITGUARD analyzes a commit in 32.4 minutes on average and achieves 75.36% average coverage of modified functions.</details> |

## Distributed Systems

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Generalizing and accelerating consistency checking for non-transactional distributed storage systems](https://arxiv.org/abs/2608.17388v1)** | ⭐ 82/100 | 提出通用化线性一致性检测算法 | 算法改进显著提升检测效率并发现多个生产环境Bug | <details><summary>展开</summary>Linearizability checkers check if an operation history, observed by concurrent clients, is linearizable. They are used in testing distributed storage systems, and use the classic Wing-Gong (WG) linearizability checking algorithm. In this paper, we generalize the WG algorithm to make linearizability checkers more versatile: we can check other non-transactional consistency guarantees, like ordered sequential consistency provided by Zookeeper. Equipped with this generalization, we can also check for system-specific consistency guarantees that introduce additional ordering constraints over operations in a history, as per the system's specification. Our experiments with 8 distributed storage systems show that checking for system-specific consistency guarantees is easy to realize, reduces false negatives in testing, helps debug consistency violations, can be up to 370x faster, and can scale to more concurrent clients within the same checking time budget. We report 6 new consistency violation bugs, out of which 5 could not be found with existing consistency checkers.</details> |
| **[SpecTrum: Specification-Guided Differential Fuzzing for Ethereum Consensus Clients](https://arxiv.org/abs/2608.17738v1)** | ⭐ 82/100 | 基于规范引导的以太坊共识客户端差分模糊测试框架 | 通过形式化规范提升了共识客户端的测试覆盖率与安全性 | <details><summary>展开</summary>Ethereum's consensus safety relies on independent consensus client implementations agreeing on every state transition. When they diverge due to implementation errors, the network can fork, finality can stall, and severe attacks are possible. To prevent such consensus divergences, Ethereum provides a Python reference implementation (consensus-spec), which acts as a specification, and a hand-crafted official test suite (spectests). However, as an executable implementation, Ethereum's specification defines validity implicitly through runtime behavior. As a result, it lacks a systematic way to ensure that all validity conditions are thoroughly evaluated. We present SpecTrum, a framework that addresses this problem in three stages. First, we introduce Consensus-SpecTec, a mechanized specification of the Ethereum consensus algorithm, which makes validity conditions explicit as if-premises. Second, we define premise coverage, a metric that measures which if-premises are evaluated to true and false across spectests. Third, we develop a specification-based test generator that extracts constraints on premises not evaluated to false by spectests and generates inputs to evaluate them. Applying SpecTrum to five major Ethereum consensus clients, we identify 27 cross-client divergence cases, 22 of which cannot be found without the premises inserted in our mechanization. All 27 cases reproduce across fork versions, and extending the mechanized specification to a new fork takes modest effort proportional to the specification difference.</details> |


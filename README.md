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

## 2026-08-09

## Network Stack & Protocol

| 标题 | 评分 | Gemini 摘要 | 评分理由 | 原始摘要 |
|------|------|-------------|----------|----------|
| **[Dart: An Automated and Reproducible Environment Toolkit for DNS Protocol Analysis](https://arxiv.org/abs/2608.04498v1)** | ⭐ 70/100 | Dart提供DNS协议分析的自动化编排工具 | 工具实用性强，但属于研究辅助设施而非核心系统架构创新 | <details><summary>展开</summary>Domain Name System (DNS) protocol analysis is fundamental to understanding and fortifying the Internet naming infrastructure. However, the lack of automated, portable, and user-friendly environment orchestration tools imposes significant overhead on researchers and severely limits the reproducibility of DNS studies. In this paper, we present Dart, an automated toolkit specifically engineered for DNS protocol analysis. Dart employs a declarative syntax to abstract the intricate software dependencies and heterogeneous configuration requirements of diverse DNS implementations, providing a unified and streamlined orchestration interface. We describe the architecture of Dart and evaluate its performance. Furthermore, we present two case studies that illustrate how Dart enables researchers to construct portable DNS analysis environments with a single command. To foster transparency and facilitate future research, all replicated environments and configurations will be open-sourced.</details> |
| **[Measuring Post-Quantum TLS Deployment Across UK Internet Sectors](https://arxiv.org/abs/2608.02147v1)** | ⭐ 70/100 | 量化评估英国互联网基础设施的后量子密码部署现状 | 通过大规模实测揭示了PQC在网络协议中的部署差异与瓶颈 | <details><summary>展开</summary>Post-quantum cryptography (PQC) is becoming an important component of long-term trust in Internet-facing infrastructure. Publicly observable PQC support provides evidence of externally visible deployment, but does not necessarily reflect the overall progress of an organisation's post-quantum migration. This distinction matters when observable deployment is used as an indicator of organisational readiness or progress towards migration deadlines. We present a measurement study of observable PQC deployment across 4,665 UK organisations spanning ten sectors. We measure post-quantum key-exchange support across HTTPS and SMTP STARTTLS endpoints, attribute reachable endpoints to their underlying infrastructure providers where possible, and statistically examine protocol-, sector-, and provider-level deployment patterns. Among reachable endpoints, 44.0\% of HTTPS services supported at least one evaluated PQC key-exchange group, compared with 6.4\% of SMTP services. Among organisations reachable over both protocols, HTTPS support was significantly more common than SMTP support (matched odds ratio 16.89). Although deployment varied across sectors, infrastructure provider identity was substantially more predictive than organisational sector, and observable deployment was highly concentrated among a small number of providers. Only 144 organisations supported PQC across both web and email infrastructure, highlighting an uneven and fragmented migration landscape. No post-quantum certificate signatures were observed across the measured endpoints. These findings show that observable PQC deployment is currently shaped predominantly by infrastructure-provider deployment decisions and should not be interpreted as a complete measure of organisational migration readiness.</details> |
| **[Deployment Feasibility Analysis of Post-Quantum Digital Signatures in Safety-Critical C-V2X Communication for Urban Mobility Scenario](https://arxiv.org/abs/2608.05087v1)** | ⭐ 70/100 | 分析C-V2X中后量子签名部署可行性 | 针对车载网络协议栈的实证分析，具有工程参考价值 | <details><summary>展开</summary>The transition from the classical ECDSA to PQC creates substantially larger authentication payloads for safety-critical C-V2X sidelink communication. This study determines which NIST post-quantum signature algorithms are compatible with the current SAE J3161 deployment profile and quantifies their communication-level effects. A transport-block feasibility analysis was performed using IEEE 1609.2 secured-message structures, SAE J3161 radio parameters, and the signature and public-key sizes of ECDSA P-256, Falcon-512, Dilithium-2, and SPHINCS+. Falcon-512, the only post-quantum candidate that fit the applicable transport-block constraints, was compared with ECDSA P-256 through full-stack C-V2X PC5 Mode 4 co-simulation. The evaluation covered 24 scenarios spanning six traffic levels-of-service with line-of-sight and non-line-of-sight propagation. PDR and end-to-end latency were evaluated at a roadside unit receiver. Dilithium-2 and SPHINCS+ exceeded the available transport-block capacity, whereas Falcon-512 remained physically feasible. Falcon-512 maintained mean latency near 52 ms and 95th-percentile latency within 97-98 ms, but met the 90% packet-delivery threshold only at traffic level-of-service A, under line-of-sight propagation. ECDSA met the threshold through traffic level-of-service C. Neither algorithm met the threshold under non-line-of-sight propagation. The study provides a standards-grounded cross-layer evaluation that identifies both algorithm feasibility and traffic-dependent deployment boundaries for post-quantum signatures on C-V2X Mode 4 sidelink. The results show that spectrum efficiency, rather than cryptographic computation time, is the primary deployment constraint. They support standards development concerning payload structure, resource allocation, certificate transmission, and migration strategies for quantum-resistant vehicular communication.</details> |


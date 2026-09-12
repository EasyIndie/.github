<div align="center">

<img src="https://raw.githubusercontent.com/EasyIndie/.github/main/assets/EasyOPC-banner-profile.png" alt="EasyOPC — AI 时代一人公司基础设施建设" width="100%" />

**AI 时代一人公司（OPC）基础设施建设**

*One-Person Company infrastructure for the AI era.*

<br />

[![Website](https://img.shields.io/badge/官网-opc.jokerhub.cn-0ea5e9?style=flat-square&logo=googlechrome&logoColor=white)](https://opc.jokerhub.cn)
[![X](https://img.shields.io/badge/X-@EasyOPC666-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/EasyOPC666)
[![Repositories](https://img.shields.io/badge/Repositories-14-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/orgs/EasyIndie/repositories)
[![OPC Docs](https://img.shields.io/badge/Docs-什么是%20OPC-10b981?style=flat-square&logo=readthedocs&logoColor=white)](https://github.com/EasyIndie/.github/blob/main/docs/opc.md)
[![Location](https://img.shields.io/badge/Location-China-red?style=flat-square&logo=googlemaps&logoColor=white)](#)

</div>

---

## 🧭 我们在做什么

> **OPC（One-Person Company，一人公司）**：由一个创始人运营，通过技术、自动化工具、外包与 AI Agent 扩展能力，完成过去需要多人团队才能完成的商业活动。

它不是「一个人硬扛所有事」，而是把**可复用的能力沉淀成 AI 员工、自动化系统与商业资产**，让一个人拥有一支团队的产能。

```text
OPC = 一个人 + AI 员工 + 自动化系统 + 商业资产
```

| 组成 | 角色 |
|:--|:--|
| **一个人** | 创始人 · 决策与方向 |
| **AI 员工** | 开发 · 内容 · 研究 · 运营 Agent |
| **自动化系统** | 工作流 · CI · 网关 · 编排 |
| **商业资产** | 产品 · 内容 · 模板 · 数据 |

**四条业务线**：内容生产（广告 / 课程 / 推广）、软件开发（SaaS 订阅）、服务咨询（自动化与 AI 员工落地）、商业资产（模板 / Skill / 课程 / 代码库）。

---

## 🧱 项目矩阵

### 🤖 AI 员工与 Agent 协作

| 项目 | 简介 | 技术栈 |
|:--|:--|:--|
| [**EasyTeam**](https://github.com/EasyIndie/EasyTeam) | 快速组建 AI 智能体团队：软件开发 / 内容 / 视频 / 全能公司等团队模板，覆盖多种 Agent 平台 | Shell |
| [**EasyGithub**](https://github.com/EasyIndie/EasyGithub) | GitHub 上的 AI 软件开发流水线：`Issue → GitHub Actions → Agent Runner → Pi → PR`，打上 `ai` 标签即可让 Agent 提 PR | TypeScript |
| [**EasyProject**](https://github.com/EasyIndie/EasyProject) | AI Native 工程规范模板（非代码模板）：六层职责结构 + Agent 协作规范，任何 Agent 几秒内读懂项目 | Shell |
| [**EasyIndieSkill**](https://github.com/EasyIndie/EasyIndieSkill) | 内容自动化统一 AI 技能包（技能名 `easyindie`），丢给 Claude Code / Hermes / OpenClaw / Cursor 等即可用；YouTube 为首个领域 | Python |

### 🎬 内容生产

| 项目 | 简介 | 技术栈 |
|:--|:--|:--|
| [**EasyContentCreator**](https://github.com/EasyIndie/EasyContentCreator) | 面向 AI 与科技知识的自动化内容创作流水线（FastAPI API + Worker + React Web），当前处于工程底座建设阶段 | Python / TypeScript |

### 🛠️ 基础设施与自托管服务

| 项目 | 简介 | 技术栈 |
|:--|:--|:--|
| [**EasyAI**](https://github.com/EasyIndie/EasyAI) | 可本地运行的统一 LLM 网关：OneAPI 统一 `/v1/*` 入口 + LiteLLM 上游适配 + Batch Worker + Dashboard / Chat UI | TypeScript |
| [**EasyBot**](https://github.com/EasyIndie/EasyBot) | 多平台 IM 网关：Telegram / Discord / 飞书 / QQ / 微信 统一 `PlatformAdapter`，对外提供一致的 REST + WebSocket 接口，支持动态插件 | Rust |
| [**EasyBot-Registry**](https://github.com/EasyIndie/EasyBot-Registry) | EasyBot 官方插件市场目录：`catalog.json` 索引 + Releases 元数据 + ed25519 签名校验 | JSON |
| [**easybot-hello-adapter**](https://github.com/EasyIndie/easybot-hello-adapter) | EasyBot 插件开发参考示例（echo 适配器）：最小可跑 + 配套插件开发指南 | Rust |
| [**EasyGate**](https://github.com/EasyIndie/EasyGate) | 内网服务快速上公网的统一入口网关：Cloudflare Tunnel + Traefik 自动发现，无需公网 IP、无需开放路由器端口，支持 WebSocket | Shell |
| [**EasyNet**](https://github.com/EasyIndie/EasyNet) | 境外 VPS 代理部署方案：Xray+Reality / Hysteria2 / Shadowsocks 2022 / WireGuard，内置混淆对抗 DPI，一键无交互部署 | Shell |
| [**EasyWork**](https://github.com/EasyIndie/EasyWork) | 一条命令配置好开发环境：模块化安装 / 卸载、shell 补全、dry-run 预览 | Shell |

### 📚 工程实践与知识沉淀

| 项目 | 简介 | 技术栈 |
|:--|:--|:--|
| [**EasyAndroid**](https://github.com/EasyIndie/EasyAndroid) | Android 真机开发实践沉淀：无 IDE 纯命令行构建、ADB 多设备、厂商侧载封锁与绕行，均来自真机验证 | Shell / Kotlin |
| [**`.github`**](https://github.com/EasyIndie/.github) | 本组织主页与公共资源（品牌资源、OPC 文档） | Markdown |

---

## 🏗️ 架构全景

<div align="center">

<img src="https://raw.githubusercontent.com/EasyIndie/.github/main/assets/architecture.svg" alt="一人公司基础设施架构图：AI 员工层 / 能力与数据层 / 生产与自动化层 / 获客与变现层 / 基础环境，高亮为 EasyIndie 自研项目，底部为数据反馈闭环" width="100%" />

**五层结构：AI 员工 → 能力与数据 → 生产与自动化 → 获客与变现 → 基础环境**，并以数据反馈闭环收口。
高亮标注的为 EasyIndie 自研项目，其余为可替换的第三方工具或集成。

</div>

> 完整架构说明与工具选型见官网 **[opc.jokerhub.cn](https://opc.jokerhub.cn/#architecture)**。

---

## 🚀 如何参与

- ⭐ **Star** 你感兴趣的项目，这是最直接的支持
- 🐛 通过 **Issue** 反馈问题或提出需求；标上 `ai` 标签的仓库可触发 AI 自动修复流程（见 [EasyGithub](https://github.com/EasyIndie/EasyGithub)）
- 🧩 为 [EasyBot](https://github.com/EasyIndie/EasyBot) 开发插件并上架 [插件市场](https://github.com/EasyIndie/EasyBot-Registry)
- 📖 阅读 [什么是 OPC](https://github.com/EasyIndie/.github/blob/main/docs/opc.md)，用这套基础设施搭建你自己的「一人公司」

---

<div align="center">

**EasyOPC** · [官网](https://opc.jokerhub.cn) · [X / Twitter](https://x.com/EasyOPC666) · [全部仓库](https://github.com/orgs/EasyIndie/repositories)

<sub>用一个人 + AI，做一支团队的事。</sub>

</div>

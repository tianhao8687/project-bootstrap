# Project Bootstrap

> **带来一个模糊想法，拿走三个可以直接开始 AI 开发的文件。**

Project Bootstrap 是一个面向 AI 开发的项目启动 Skill，特别适合不会写代码、只有模糊想法，或者不想在开发前先写一堆复杂文档的人。

它会在一个对话中，把一个模糊想法变成三个独立、正式的 Markdown 文件：

- `PROJECT_BRIEF.md` —— 做什么，为什么做
- `PROJECT_PLAN.md` —— 怎么做，项目到底多复杂
- `AI_PROJECT_RULES.md` —— 后续 AI 应该如何执行，避免跑偏、重复劳动和擅自扩大范围

**语言：** [English](README.md) · 简体中文

---

## 为什么做这个项目

很多 AI 编程项目真正出问题，并不是因为代码本身，而是项目还没正式开始就乱了。

常见问题包括：

- 一个模糊想法被 AI 自动扩成复杂大系统
- 每个 AI 对话都重新读取整个项目
- 多个 AI 角色重复分析同一个问题
- 已经解决的问题没有新证据却被反复重开
- AI 偷偷修改需求或架构
- 简单项目被强行组建复杂团队
- 没真正运行测试，却报告“已通过”

Project Bootstrap 的目标，就是在正式开发之前先把这些问题挡住。

---

## 三文件管线

```text
模糊想法
↓
PROJECT_BRIEF.md
定义 WHAT + WHY
↓
PROJECT_PLAN.md
定义 HOW + 复杂度 + 路线图
↓
AI_PROJECT_RULES.md
定义后续 AI 执行规则
↓
正式开发开始
```

三个文件完成后，Project Bootstrap Skill 结束。

真实开发项目只需要携带这三个正式文件，不需要继续加载整个规划 Skill。

---

## Solo / Lean / Team

Project Bootstrap 会自动判断项目应该采用哪种执行模式。

### Solo

适合简单项目，一个 AI 就能稳定完成。

不组假团队，不制造多余流程。

### Lean

适合需要少量独立专业判断的项目，例如开发、测试、技术审查。

通常只启用 2～4 个真正必要的角色。

### Team

只适合真正复杂的项目，例如同时涉及：

- Migration
- Worker / Queue
- 多 Provider
- 真实付费能力
- 敏感数据
- 复杂 AI 工作流
- 长期多阶段开发

核心原则：

> **项目多简单，治理就多简单；项目多复杂，治理才多复杂。**

---

## 自由思考，授权行动

Project Bootstrap 不是为了限制 AI 的能力。

它把“思考”和“行动权限”分开：

- **Level 1：** 低影响实现细节，AI 可以自主决定
- **Level 2：** AI 可以提出更优建议，但不能偷偷修改正式决定
- **Level 3：** 修改已确认范围、核心架构、硬约束、真实支付、生产迁移等高风险边界，必须先获得明确批准

核心原则：

> **AI 的思考不受限制，行动受权限约束。**

---

## 为什么三个文件必须分开

这是故意这样设计的。

后续 AI 不应该每次任务都重新读取整个项目。

正确方式是：

```text
需要理解 WHAT / WHY / 产品边界？
→ 读 PROJECT_BRIEF.md

需要理解 HOW / 当前阶段 / 技术路线？
→ 读 PROJECT_PLAN.md

正在执行真实开发？
→ 遵守 AI_PROJECT_RULES.md

不得默认每次重新读取全部三个文件。
```

三个文件强制分离，是为了支持最小上下文加载，并减少无关 Token 消耗。

---

## 仓库结构

```text
project-bootstrap/
├── README.md
├── README_CN.md
├── LICENSE
├── en/
│   ├── SKILL.md
│   ├── THREE_MD_PIPELINE_SPEC.md
│   └── templates/
│       ├── PROJECT_BRIEF.md
│       ├── PROJECT_PLAN.md
│       └── AI_PROJECT_RULES.md
└── zh-CN/
    ├── SKILL.md
    ├── THREE_MD_PIPELINE_SPEC.md
    └── templates/
        ├── PROJECT_BRIEF.md
        ├── PROJECT_PLAN.md
        └── AI_PROJECT_RULES.md
```

---

## 使用方法

1. 选择语言：
   - English：[`en/`](en/)
   - 简体中文：[`zh-CN/`](zh-CN/)

2. 把对应语言版本的 `SKILL.md` 加载到你的 AI 环境。

3. 直接给出一个模糊想法，例如：

   > 我想做一个帮助自由设计师整理客户资料的软件。

4. 确认生成的 `PROJECT_BRIEF`。

5. 确认生成的 `PROJECT_PLAN`。

6. 最终拿到三个独立正式文件：

```text
PROJECT_BRIEF.md
PROJECT_PLAN.md
AI_PROJECT_RULES.md
```

7. 新建真实开发项目，只导入这三个文件。

---

## Project Bootstrap 不是什么

它不是：

- 编程框架
- 运行时依赖
- 宣称保证节省固定比例 Token 的基准测试
- 技术判断的替代品
- 保证所有 AI 模型都给出完全相同结果的系统

它是一个轻量的项目定义、规划和 AI 执行治理层。

---

## 当前验证状态

v1.6 已通过当前规则级和结构级压力测试：

- 69 / 69 静态与一致性检查
- 96 / 96 规则级压力场景
- 6 维复杂度基础评分全部 729 种组合
- 5,000 次随机复杂度变异
- 阈值错误：0
- 单调性错误：0
- 随机变异错误：0

重要说明：这些结果**不是跨模型真实会话测试结果**。不同模型、不同产品中的实际表现仍可能不同。

---

## 设计原则

- 一个 Skill、一个对话、三个最终 MD
- 少提问，主动推荐
- 没有新证据，不重新全面分析
- 一个问题只设一个主负责人
- 禁止多个 AI 重复劳动
- 通过时少说，失败时说清
- 局部修改只影响局部
- 简单项目 → 简单规则
- 复杂项目 → 更强治理
- AI 可以自由思考，但行动必须有对应权限

---

## 版本

当前版本：**v1.6**

---

## License

MIT License，详见 [`LICENSE`](LICENSE)。

Copyright © 2026 tianhao8687

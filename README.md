# Project Bootstrap

> **Bring one rough idea. Leave with three files ready for AI development.**

Project Bootstrap is a planning Skill for people who want to build software with AI without letting the project become chaotic before development even starts.

It turns one rough idea into three separate, formal Markdown files:

- `PROJECT_BRIEF.md` — what to build and why
- `PROJECT_PLAN.md` — how to build it and how complex the project really is
- `AI_PROJECT_RULES.md` — how later AI should execute without drifting, duplicating work, or expanding scope without permission

**Language:** English · [简体中文](README_CN.md)

---

## A key change in v1.8

**Conversation explains and confirms; Markdown stores memory and execution.**

Formal files no longer persist full score breakdowns, why other modes were rejected, confidence explanations, long alternative comparisons, or ordinary unconfirmed suggestions by default.

Before content enters formal Markdown, ask one question:

> Would a future AI be more likely to make a wrong execution decision if it did not know this?

Only content with a real execution consequence belongs in formal project memory.


---

## v1.8: Read Existing Facts First and Ask Only Blocking Questions

v1.8 keeps the same three-file output while improving the startup judgment layer:

- Do not ask again when an answer already exists in conversation, files, or project documents.
- When a project already exists, read current facts first instead of restarting from blank questions.
- Classify unknowns as blocking, non-blocking, or irrelevant; only blocking questions interrupt by default.
- AI owns technical route, architecture, security, data-boundary, and test-sufficiency judgment instead of pushing technical correctness onto a non-technical user.
- Use only three evidence states: `Confirmed`, `Pending confirmation`, and `Unverified`.
- Add a final three-file gate for duplication, evidence state, empty sections, context rules, and current-stage acceptance.
- Final handoff stays in conversation and does not become a fourth formal source file.

The core promise remains unchanged:

> **One idea. One conversation. Three formal files. Then the Skill exits.**

---

## v1.8.3: Tell the user the important difficulties directly

The hidden-complexity scan no longer stays entirely inside the AI.

When a project contains real difficulties the user is likely to underestimate—and those difficulties could cause rework, higher cost, or architectural change—the AI first shows a visible warning:

> ⚠️ **This is important. Please read this first.**

It then explains only 2–4 key difficulties in plain language. The tone may be slightly sharp or humorous, but it does not become a formal report, create a fourth file, or repeat the same warning across later turns without new evidence.

---

## Why this exists

AI coding often fails before the code is the real problem.

Common failure modes:

- a vague idea becomes an over-engineered system
- every AI chat rereads the whole project
- multiple AI roles repeat the same analysis
- solved issues are reopened without new evidence
- AI silently changes requirements or architecture
- small projects get unnecessary teams and process
- tests are reported as passed even when they were not actually run

Project Bootstrap tries to stop those problems before implementation starts.

---

## The three-file pipeline

```text
Rough idea
↓
PROJECT_BRIEF.md
Defines WHAT + WHY
↓
PROJECT_PLAN.md
Defines HOW + complexity + roadmap
↓
AI_PROJECT_RULES.md
Defines execution rules for later AI
↓
Real development begins
```

The planning Skill exits after the three files are complete.

The real development project should carry only the three formal files, not the whole planning Skill.

---

## Solo / Lean / Team

Project Bootstrap routes a project into one of three execution modes:

### Solo

For simple projects that one AI can complete reliably.

No fake team. No unnecessary process.

### Lean

For projects that need a small number of distinct professional judgments, such as implementation, testing, or technical review.

Usually 2–4 necessary roles.

### Team

Only for genuinely complex projects with multiple interacting boundaries, such as migrations, queues, multiple providers, paid capabilities, sensitive data, complex AI workflows, or long multi-stage development.

The rule is simple:

> The simpler the project, the simpler the governance.

---

## Freedom to think. Permission to act.

Project Bootstrap does not try to make AI less intelligent.

It separates thinking from authorization:

- **Level 1:** low-impact implementation details may be decided autonomously
- **Level 2:** better ideas may be suggested, but formal decisions cannot be changed silently
- **Level 3:** changes to confirmed scope, core architecture, hard constraints, payments, production migrations, or other high-risk boundaries require explicit approval

Core principle:

> **AI thinking is unrestricted; AI action is permission-controlled.**

---

## Why the three files must stay separate

This is intentional.

Later AI should not reread the entire project context for every task.

Instead:

```text
Need WHAT / WHY / product boundaries?
→ Read PROJECT_BRIEF.md

Need HOW / stage / technical direction?
→ Read PROJECT_PLAN.md

Executing the project?
→ Follow AI_PROJECT_RULES.md

Do not reread all three files by default.
```

Keeping the files separate supports progressive context loading and helps reduce irrelevant token usage.

---

## Repository structure

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

## How to use

1. Choose a language:
   - English: [`en/`](en/)
   - 简体中文: [`zh-CN/`](zh-CN/)

2. Load the language version of `SKILL.md` into your AI environment.

3. Start with a rough idea, for example:

   > I want to build a tool that helps freelance designers organize client materials.

4. Confirm the generated `PROJECT_BRIEF`.

5. Confirm the generated `PROJECT_PLAN`.

6. Receive three separate formal Markdown files:

```text
PROJECT_BRIEF.md
PROJECT_PLAN.md
AI_PROJECT_RULES.md
```

7. Create the real development project and import only those three files.

---

## What Project Bootstrap is not

It is not:

- a coding framework
- a runtime dependency
- a benchmark claiming guaranteed token savings
- a replacement for technical judgment
- a guarantee that every AI model will make identical decisions

It is a lightweight planning and governance layer designed to make AI-assisted software projects easier to start and harder to derail.

---

## Validation status

v1.8 has passed the current rule-level and structural stress suite:

- 69 / 69 static and consistency checks
- 96 / 96 rule-level stress scenarios
- all 729 combinations of the six-dimension base complexity score
- 5,000 random complexity mutations
- 0 threshold errors
- 0 monotonicity errors
- 0 random mutation errors

Important: these results are **not** cross-model live-session results. Real behavior may still vary across models and products.

v1.8.3 also adds local rule-level stress tests for the user-visible important-difficulty reminder:

- 6 static rule checks
- 16 single-turn project scenarios
- 6 multi-turn conversations, 24 turns total
- 5,000 randomized multi-turn state mutations, 45,167 turns total
- Average reminder sample length: 114.5 compact characters; maximum: 128 / 320
- Current failures: 0

These checks validate rule completeness, output length, trigger conditions, multi-turn deduplication, and resistance to rule drift in sample scenarios. They do not prove that every external model will follow the Skill perfectly.

---

## Design principles

- One Skill, one conversation, three final Markdown files
- Ask less; recommend proactively
- No new evidence, no full re-analysis
- One owner per problem
- No duplicate agent work
- Pass briefly; fail with enough evidence to act
- Local changes stay local
- Simple project → simple rules
- Complex project → stronger governance
- AI can think freely; action requires the right level of permission

---

## Version

Current release: **v1.8.3**

---

## License

MIT License. See [`LICENSE`](LICENSE).

Copyright © 2026 tianhao8687

---
name: project-bootstrap
description: For people who cannot code, only have a rough idea, or do not want to write complex documents before starting. In one conversation, turn an idea into PROJECT_BRIEF.md, PROJECT_PLAN.md, and AI_PROJECT_RULES.md. First define what to build, then plan how to build it and determine project complexity, and finally generate the most suitable AI execution rules for Solo / Lean / Team mode. Ask fewer questions by default, recommend proactively, confirm only where needed, and never make a simple project unnecessarily complex.
---

# Project Bootstrap

## Goal

Complete three formal project files in one conversation:

1. `PROJECT_BRIEF.md`
   - Answers: What are we building, why are we building it, who is it for, and what should the first version do?

2. `PROJECT_PLAN.md`
   - Answers: How should it be built, what stages are needed, what technical capabilities are required, and how complex is the project?

3. `AI_PROJECT_RULES.md`
   - Answers: How should AI execute the project, are multiple roles actually needed, and what rules must be followed?

After all three files are complete, this Skill ends.

The real development project should import only these three files. It does not need to keep loading this Skill.

---

# 1. Highest Principles

1. One Skill, one conversation, three final Markdown files.
2. Ask as few questions as possible by default, with at most 1–3 simple questions per round.
   - Once there is enough information to produce a reviewable draft, produce the draft first. Do not keep interrogating the user in pursuit of perfection.
   - Ask more only when an unknown could materially change the project goal, complexity mode, core architecture, or a high-risk boundary.
3. When the user does not know, recommend proactively instead of asking endlessly.
4. AI suggestions must be kept separate from facts and decisions already confirmed by the user.
5. A later stage may fill in information that an earlier stage left undefined, but it must never silently rewrite a confirmed upstream decision.
6. When the user changes only one part, update only the affected parts. Do not regenerate everything.
7. Do not automatically expand a small project into a large SaaS, enterprise platform, multi-tenant system, or complex AI team.
8. The simpler the project, the simpler the rules. The more complex the project, the stronger the governance.
9. Use the "shortest sufficient output" principle: enough to act, no filler.

---

# 2. How to Start

Do not begin by forcing the user to fill out a complicated form.

The user only needs to say one sentence, for example:

```text
I want to build software that helps Amazon designers organize customer materials.
```

Or:

```text
I have an idea, but I do not know exactly what to build. Please recommend something.
```

Automatically enter the appropriate mode:

- **Organize Mode**: the user is already relatively clear.
- **Guided Mode**: the user only has a rough idea.
- **Recommendation Mode**: the user does not know, explicitly asks for recommendations, or cannot answer a key question twice in a row.

When the mode can be inferred, do not force the user to choose one.

---

# 3. Overall Workflow

```text
User idea
↓
Stage 1: Project Definition
↓
Generate PROJECT_BRIEF draft
↓
User confirms
↓
Stage 2: Project Plan
↓
Determine complexity: Solo / Lean / Team
↓
Generate PROJECT_PLAN draft
↓
User confirms
↓
Stage 3: Generate AI_PROJECT_RULES
↓
Output three formal Markdown files at once
↓
Skill ends
```

Keep only two major confirmation points by default:

1. Confirm `PROJECT_BRIEF`
2. Confirm `PROJECT_PLAN`

The third file is generated directly from the first two by default. Ask again only when a major conflict is found.

---

# 4. Stage 1: Generate PROJECT_BRIEF.md

## Goal

Resolve WHAT and WHY only.

At minimum, clarify:

- One-sentence project definition
- Real problem
- Target users
- Core scenarios
- Core inputs
- Core outputs
- Must-have MVP capabilities
- Explicit non-goals
- Success criteria
- Confirmed decisions
- Unconfirmed suggestions
- Real-world risks

## Question Order

Ask only what is needed. Do not mechanically ask every question.

Priority order:

```text
What problem do you most want to eliminate?
↓
Who will use it?
↓
When would they open it?
↓
What do users give it?
↓
What do they want to get back?
↓
If version one could solve only one problem, which is the most important?
```

## Recommendation Mode

When the user does not know, output one primary recommendation:

```text
[AI RECOMMENDATION]

Project goal:

Core users:

Version one should only do:
1.
2.
3.

Not now:
1.
2.
3.

Why:

Choose:
A. Continue with this
B. Change a few things
C. Recommend again
```

Give one primary plan by default. Do not dump multiple complex routes on the user at once.

Exception:

> When the user explicitly requests multiple options, provide them, but keep the number controlled and clearly identify the primary recommendation.

## Reality Check

Before formal confirmation, check only:

- Is it obviously infeasible?
- Does it depend on data or permissions that are currently unavailable?
- Is there a major privacy, security, legal, or cost risk?
- Is it already obviously over-engineered?
- Is there a smaller, more realistic first version?

Keep this lightweight. Do not perform a full technical review yet.

## Fixed PROJECT_BRIEF.md Structure

```markdown
# PROJECT_BRIEF

## 1. One-Sentence Project Definition

## 2. Why This Project Exists

## 3. Target Users

## 4. Core Pain Points

## 5. Core Use Cases

## 6. Core Inputs

## 7. Core Outputs

## 8. Must-Have MVP Capabilities

## 9. Explicit Non-Goals

## 10. Success Criteria

## 11. Confirmed Decisions

## 12. AI Suggestions Not Yet Confirmed

## 13. Open Questions

## 14. Real-World Risks
```

After generating the draft, ask only:

```text
A. Confirm and continue to the project plan
B. Mostly good; I want to change a few things
C. Not right; reorganize it
```

---

# 5. Stage 2: Generate PROJECT_PLAN.md

## Input

Must inherit the confirmed `PROJECT_BRIEF.md`.

## Goal

Resolve HOW only.

Plan according to the actual project:

- Overall technical direction
- System structure
- Core modules
- Data boundaries
- Security and cost boundaries
- Whether AI / Provider / Worker / Queue are actually needed
- Project complexity
- Execution mode
- Evidence for the complexity judgment
- Necessary AI roles
- Stage roadmap
- Acceptance criteria for each stage
- Conditions for enabling high-risk capabilities
- First execution stage

## Iron Rule

Never silently modify confirmed content in `PROJECT_BRIEF.md`.

When a conflict is found, output:

```text
[CONFLICT FOUND]

PROJECT_BRIEF already confirmed:
...

Current technical planning found:
...

Recommendation:
...

Choose:
A. Keep the original decision
B. Accept the adjustment
```

---

# 6. Project Complexity Router

Do not ask a non-technical user to decide whether the project is "large."

AI should automatically perform a three-layer judgment based on `PROJECT_BRIEF.md`:

```text
Layer 1: Base complexity
↓
Layer 2: Which independent professional judgments are needed?
↓
Layer 3: Forced upgrade conditions
↓
Final output: Solo / Lean / Team
```

Important:

> Do not judge from code size, number of pages, or number of features alone.
> What matters is how many independent complexity boundaries exist and whether those boundaries require different professional judgments.

---

## 6.1 Layer 1: Six-Dimension Base Complexity

Score each dimension only 0 / 1 / 2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Product scope | One clear goal | Several related capabilities | Multiple strongly interdependent modules |
| System structure | Single page / script / simple monolith | Frontend + backend or several major modules | Async jobs, multiple services, complex chains |
| Data complexity | No database or simple storage | Formal database | Complex relationships, migrations, historical compatibility |
| External dependencies | No key dependency | Ordinary API or one provider | Multiple providers, payments, critical external services |
| Risk boundaries | Almost no special risk | Login, permissions, cost, etc. | Sensitive data, payments, finance, healthcare, major security or compliance |
| Long-term evolution | One-off tool, small utility, or no confirmed long-term maintenance | User explicitly confirms ongoing iteration | Multi-stage long-term project with explicit historical compatibility, version migration, or long-term maintenance needs |

Use the base score only for an initial tendency:

```text
0–3
→ Tend Solo

4–7
→ Tend Lean

8–12
→ Tend Team
```

This score is not the final conclusion.

Special rule:

> Never add points to "long-term evolution" merely because any software could theoretically continue to evolve. Count 1–2 points only when the user explicitly confirms ongoing iteration or the project objectively requires historical compatibility, version migration, and long-term maintenance.

Avoid double counting:

> If several dimensions are merely different symptoms of the same root cause, explain the relationship. Do not mechanically inflate the score.

---

## 6.2 Layer 2: Independent Professional Judgment Needs

Check whether the project genuinely needs independent:

- Product judgment
- Technical architecture judgment
- AI workflow judgment
- Security / cost judgment
- Testing / delivery judgment

Decision logic:

```text
One AI can complete it reliably
→ Solo

Needs 2–4 distinct professional judgments
→ Lean

Multiple professional boundaries coexist and may conflict
→ Team
```

Do not create a full team merely because the project sounds advanced.

---

## 6.3 Layer 3: Forced Upgrade Conditions

When any of the following appears, the project should usually be upgraded to at least `Lean`:

- Real payments
- Formal login and permissions
- Real paid AI provider
- Production database migration
- Sensitive user data
- Critical third-party API
- A key business failure would cause clear loss

Consider `Team` when multiple high-risk boundaries coexist, for example:

- Complex database migrations
- Worker / Queue
- Multiple providers
- Real paid capabilities
- Sensitive data
- Complex AI workflows
- Long, multi-stage development
- Multiple professional reviews running in parallel over time

Do not automatically upgrade to Team because of a single risk point.

---

## 6.4 The Three Execution Modes

### Solo: Single-AI Execution

Use when:

- Functionality and boundaries are simple
- One AI can complete the project reliably
- There are no major high-risk boundaries

Do not enable a multi-role team by default.

---

### Lean: Lightweight Collaboration

Use when:

- The project has frontend + backend, a database, an AI provider, or a meaningful business workflow
- Testing or technical review is useful
- A full multi-role team is unnecessary

Usually enable only 2–4 necessary roles.

---

### Team: Multi-Role Team

Use only for genuinely complex projects, such as those combining:

- Complex business rules
- Data migrations
- Worker / Queue
- Multiple providers
- Real paid capabilities
- AI workflows
- Security boundaries
- Long multi-stage development

Principle:

> Enable a role only when that professional judgment is missing.
> Do not enable roles that are not needed.

---

## 6.5 Complexity Judgment Output Format

`PROJECT_PLAN.md` must state:

```text
[PROJECT COMPLEXITY JUDGMENT]

Recommended mode:
Solo / Lean / Team

Base score:
X / 12

Main complexity factors:
- ...
- ...

Professional judgment needs:
- Product: Needed / Not needed / Conditional
- Technical architecture: Needed / Not needed / Conditional
- AI workflow: Needed / Not needed / Conditional
- Security / cost: Needed / Not needed / Conditional
- Testing / delivery: Needed / Not needed / Conditional

Forced upgrade conditions:
None / Yes, specifically ...

Why not a lighter mode:
...

Why a heavier mode is unnecessary:
...

Confidence:
High / Medium / Low

If confidence is Low:
- Ask only 1 question: the one that most affects Solo / Lean / Team routing.
- Do not keep asking in pursuit of perfection.
- If existing information is already enough for a reviewable draft, produce the draft first and let the user correct it.

Final recommendation:
...
```

Confidence principles:

- High: main complexity boundaries are confirmed and key facts are sufficient.
- Medium: some information is unconfirmed, but it is unlikely to materially change the current mode judgment.
- Low: one key unknown could directly change the Solo / Lean / Team conclusion.

For an obviously simple project, compress the output. Do not fill an entire page merely to satisfy the format.

---

# 7. Roadmap Splitting Rules

Split by formal stages that can be independently accepted.

Do not keep subdividing for appearance:

```text
Stage 12
→ 12A
→ 12A-1
→ 12A-1-a
```

Split further only when a stage is clearly too large, spans multiple independent high-risk boundaries, or would become uncontrollable in one execution.

A small project may have only:

```text
Stage 1
Stage 2
Stage 3
```

Or even:

```text
Stage 1: Complete the MVP directly
```

Do not manufacture a complex roadmap.

---

# 8. Fixed PROJECT_PLAN.md Structure

```markdown
# PROJECT_PLAN

## 1. Planning Basis

## 2. Project Complexity Judgment

### 2.1 Six-Dimension Base Score

### 2.2 Independent Professional Judgment Needs

### 2.3 Forced Upgrade Conditions

### 2.4 Final Judgment Rationale

### 2.5 Confidence

## 3. Recommended Execution Mode

## 4. Overall Technical Direction

## 5. System Structure

## 6. Core Modules

## 7. Data Boundaries

## 8. Security and Cost Boundaries

## 9. Necessary AI Roles

## 10. Stage Roadmap

## 11. Acceptance Criteria by Stage

## 12. Conditions for Enabling High-Risk Capabilities

## 13. Explicitly Deferred Capabilities

## 14. First Execution Stage

### 14.1 Goal

### 14.2 Allowed Scope

### 14.3 Explicit Non-Goals

### 14.4 Acceptance Criteria

## 15. Known Technical Risks
```

After generating the draft, ask only:

```text
A. Confirm and generate project rules
B. Mostly good; I want to change a few things
C. Not right; replan it
```

---

# 9. Stage 3: Generate AI_PROJECT_RULES.md

## Input

Must inherit both:

- `PROJECT_BRIEF.md`
- `PROJECT_PLAN.md`

## Goal

Generate the fewest rules that are still sufficient to prevent AI from making the project chaotic.

Do not generate a wall of generic advice.

Do not default to full team governance.

Read the execution mode from `PROJECT_PLAN` first, then decide how deep the rules should be.

---

## 9.1 Solo Rule Generation Principles

Keep only truly necessary execution rules, for example:

- Implement only the current stage
- Do not automatically expand scope
- Prefer simple solutions
- Do not introduce unnecessary architecture
- Read only necessary files before making changes
- Report test results honestly
- Without new evidence, do not overturn confirmed decisions

Usually a few dozen lines are enough.

---

## 9.2 Lean Rule Generation Principles

Add to Solo:

- Role boundaries
- Who implements
- Who performs necessary review
- Who tests
- When a technical lead is actually needed
- Prohibition on duplicate work

Do not automatically expand into a full team constitution.

---

## 9.3 Team Rule Generation Principles

Only complex projects should cover:

- Highest project principles
- Formal fact priority
- Roles and boundaries
- Role activation rules
- Single owner per problem
- Context loading
- No duplicate analysis
- Conditions for reopening issues
- Development scope control
- Code reuse
- Database / Migration
- AI / Provider / security / cost
- Test integrity
- Completion reports
- Token efficiency
- Project-specific hard constraints
- AI freedom and action authorization

---

# 10. Fixed AI_PROJECT_RULES.md Structure

Trim dynamically according to the execution mode. Do not keep empty sections just for formality.

Suggested structure:

```markdown
# AI_PROJECT_RULES

Version: 1.0
Execution Mode: Solo | Lean | Team

Generated From:
- PROJECT_BRIEF
- PROJECT_PLAN

## 1. Project Execution Mode

## 2. Highest Project Principles

## 3. Formal Fact Priority

## 4. Currently Necessary Roles

## 5. Role Responsibilities and Prohibitions

## 6. Context Loading Rules

## 7. Scope Control Rules

## 8. No Duplicate Analysis Rules

## 9. Conditions for Reopening Issues

## 10. AI Freedom and Action Authorization

## 11. Development Execution Rules

## 12. Database / AI / Provider / Security / Cost Rules

## 13. Testing and Acceptance Rules

## 14. Completion Report Rules

## 15. Token Efficiency Rules

## 16. Project-Specific Hard Constraints

## 17. Conditions for Changing Rules
```

Rules:

- Solo: keep only the 5–8 sections that genuinely apply.
- Lean: keep the necessary 8–12 sections.
- Team: cover the full set as needed.
- Omit sections with no applicable content.

However, the following are mandatory in Solo / Lean / Team and must never be removed by dynamic trimming:

- Minimum context-loading rules
- Three-file on-demand reading rules
- Never reread all three files by default for every task

At minimum, the rules must explicitly state:

```text
AI_PROJECT_RULES.md
→ Must be followed during later execution

PROJECT_BRIEF.md
→ Read only when WHAT / WHY / product boundaries are needed

PROJECT_PLAN.md
→ Read only when HOW / stage / technical direction are needed

Do not reread all three files by default for every task.
```

---

# 11. Verifiable Rules

Bad:

```text
Try to avoid duplicate review.
```

Good:

```text
Without new evidence, do not perform a full review again for an issue that has already passed.
```

Bad:

```text
Be careful about scope.
```

Good:

```text
Do not add business capabilities that are not authorized by the current execution stage in PROJECT_PLAN.
When extra issues are discovered, record them only. Do not expand the modification scope opportunistically.
```

Bad:

```text
Pay attention to testing.
```

Good:

```text
A test that was not actually run must never be reported as "passed."
```

---

# 12. AI Freedom and Action Authorization

Core principle:

> AI thinking is unrestricted; AI action is permission-controlled.

AI may always:

- Propose new ideas
- Discover new opportunities
- Challenge old decisions
- Point out risks
- Recommend removing over-engineering
- Propose better technical approaches

But:

- A suggestion never automatically becomes a formal decision.
- A formal decision never automatically enters the current execution scope.
- AI must not treat "I found a better idea" as permission to change requirements, alter architecture, or expand scope without authorization.

Use three action levels.

## Level 1: Autonomous Decision

AI may act directly without asking.

Use only when all are true:

- Does not change formal requirements
- Does not change core architecture
- Does not touch hard constraints
- Does not expand the current execution stage
- Does not add a high-risk capability
- Is only an ordinary implementation detail, local optimization, or test implementation choice

Examples:

- Function naming
- Internal code decomposition
- Test-case implementation
- Local refactoring only when it does not change external behavior, data semantics, API contracts, formal facts, or confirmed user experience
- Ordinary implementation choices consistent with existing architecture

## Level 2: Suggest, But Do Not Execute Silently

AI may proactively suggest a better approach, but it must not silently modify a formal decision.

Keep suggestions short:

```text
[AI SUGGESTION]

Found:
...

Recommendation:
...

Why:
...

Impact:
...

Current handling:
Suggestion only. No formal decision is changed.
```

After proposing the suggestion, continue the current task by default. Do not interrupt the user for every suggestion.

Pause and request a decision only when the suggestion itself blocks the current task or continuing would create obvious rework, risk, or waste.

## Level 3: Explicit Approval Required

Explicit approval is required before changing:

- Confirmed product scope
- Project hard constraints
- Core architecture
- Main database path
- Security boundaries
- Real payments
- Real paid provider
- Production migration
- Major privacy or compliance rules
- Existing formal capabilities
- Current-stage scope by a material amount

Correct flow:

```text
Discover issue
↓
Propose change
↓
Explain evidence and impact
↓
Wait for explicit approval
↓
Update the affected formal files first
↓
Then execute
```

Highest rule:

> The goal is not to restrict AI thinking. The goal is to restrict unauthorized AI action.

---

# 13. Inheritance Relationship Between the Three Files

```text
PROJECT_BRIEF
Defines WHAT & WHY
↓
PROJECT_PLAN
May design HOW only from WHAT & WHY
↓
AI_PROJECT_RULES
May define execution rules only from WHAT + WHY + HOW
```

Highest rule:

> A later stage may fill in information that an earlier stage left undefined, but it must never silently rewrite a confirmed upstream decision.

---

# 14. Local Change Rules

When the user changes only one small point:

1. Identify affected sections.
2. Modify only the affected parts.
3. Clearly state:
   - What changed
   - What did not change
   - Whether downstream files are affected
4. Update only downstream files that are truly affected.

Do not regenerate the whole set every time.

---

# 15. Final Output

After all three files are complete, provide:

- `PROJECT_BRIEF.md`
- `PROJECT_PLAN.md`
- `AI_PROJECT_RULES.md`

Output rules:

1. If the current environment supports file creation, create three real Markdown files and provide them for direct download or import.
2. If the current environment cannot create files, output three separate Markdown blocks using the exact filenames above.
3. Always preserve and output three separate formal source files. Never merge them into one file or replace them with one master document.
4. Reason: later AI should load only the files needed for the current task, avoiding the repeated cost of reading the entire project context and reducing irrelevant token usage.
5. Do not provide only a summary while omitting the formal file contents.
6. Final files may contain only confirmed decisions as formal decisions. Unconfirmed suggestions must remain explicitly unconfirmed and must never masquerade as formal decisions.

Then tell the user briefly:

```text
Planning is complete.

Next, create the real development project and import these three files.
The real development stage does not need to keep loading this Skill.
```

---

# 16. Success Criteria

The process is complete only when all of the following are true:

```text
The user knows what they are building
+
The user knows what version one will not do
+
The user knows how the project should be implemented
+
The user knows why the project belongs in Solo / Lean / Team
+
The user knows what rules later AI must follow
+
The three Markdown files can be imported directly into the real development project
```

In one sentence:

> One conversation turns one rough idea into three formal files ready for a real AI development project.

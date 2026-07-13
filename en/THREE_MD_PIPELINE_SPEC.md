# THREE_MD_PIPELINE_SPEC

## Core Positioning

One Skill, one conversation, three formal outputs:

1. PROJECT_BRIEF.md
2. PROJECT_PLAN.md
3. AI_PROJECT_RULES.md

## Data Flow

PROJECT_BRIEF
→ Defines WHAT / WHY

PROJECT_PLAN
→ Inherits BRIEF and adds only HOW
→ Uses the Project Complexity Router to determine Solo / Lean / Team

AI_PROJECT_RULES
→ Inherits BRIEF + PLAN and generates execution rules matched to actual project complexity

## Project Complexity Router

Use three layers:

1. Six-dimension base complexity
2. Independent professional judgment needs
3. Forced upgrade conditions

Then output:

- Solo: one AI, shortest rules
- Lean: a few necessary roles
- Team: full multi-role governance only for genuinely complex projects

Do not judge from code lines, page count, or feature count alone.

## Highest Inheritance Rule

A later stage may fill in information left undefined by an earlier stage, but must never silently rewrite a confirmed upstream decision.

## AI Freedom and Action Authorization

AI may freely discover, analyze, and propose, but action is controlled by impact level:

- Level 1: Low-impact implementation details may be decided autonomously.
- Level 2: Medium-impact ideas may be suggested, but formal decisions must not be changed silently.
- Level 3: Changes to formal scope, core architecture, hard constraints, or high-risk boundaries require approval first.

The goal is not to restrict AI thinking. The goal is to restrict unauthorized AI action.

## Default Confirmation Points

Keep only two:

1. Confirm PROJECT_BRIEF
2. Confirm PROJECT_PLAN

AI_PROJECT_RULES is generated directly by default. Ask again only when a major conflict is found.

## Local Updates

When the user changes one part, update only affected sections and necessary downstream files. Do not regenerate everything.

## Exit Condition

After all three Markdown files are generated, the Skill ends.

The real development project imports only the three Markdown files and does not keep loading this Skill.

## Actual File Output Rules

- If the environment supports file creation, create three real Markdown files.
- If file creation is unavailable, output three separate Markdown blocks using the exact filenames.
- Never merge the three formal files into one.

## Long-Term Evolution Scoring Limit

Do not score long-term evolution merely because "any software could continue to evolve."
Count it only when the user explicitly confirms continued iteration or the project explicitly requires historical compatibility, version migration, or long-term maintenance.

## Complexity Judgment Confidence

The complexity router must output: High / Medium / Low.

When confidence is Low, ask only 1 question: the one that most affects Solo / Lean / Team routing.
Once information is sufficient for a reviewable draft, produce the draft instead of continuing to interrogate the user.

## Mandatory Separation of the Three Files

Final output must keep these separate:

- `PROJECT_BRIEF.md`
- `PROJECT_PLAN.md`
- `AI_PROJECT_RULES.md`

The three formal source files must remain separate and may not be replaced by one master document.

Reason: later AI should read only the files needed for the current task, avoiding irrelevant token usage from repeatedly loading the entire project context.

## Mandatory in Every Execution Mode

Whether the final mode is Solo, Lean, or Team, the following must never be removed by dynamic trimming:

- Minimum context-loading rules
- Three-file on-demand reading rules
- Never reread all three files by default for every task

These are core token-efficiency constraints.

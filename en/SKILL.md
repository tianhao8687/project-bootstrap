---
name: project-bootstrap
description: Use only to start or deliberately re-scope a software project: turn a rough idea into PROJECT_BRIEF.md, PROJECT_PLAN.md, and AI_PROJECT_RULES.md. Appropriate for new projects, projects not yet in implementation, or cases where the user explicitly wants to redefine the goal and MVP boundary. Do not use for local feature changes in an existing project, known bug fixes, code review, testing, deployment, release work, or ordinary implementation tasks.
---

# Project Bootstrap

## Scope boundary

This Skill is only responsible for **project startup and definition before implementation begins**.

Use it when:

- the user has only a rough software idea;
- the user is preparing to start a new software project;
- the user needs to define target users, the core problem, MVP boundaries, and an implementation direction;
- existing ideas or documents materially conflict and the user explicitly asks to re-scope the project.

Do not use it for:

- a local feature change in an existing project;
- a known bug fix, implementation task, refactor, code review, or test task;
- deployment, release, CI, packaging, or runtime troubleshooting;
- answering one technical question or writing one standalone function.

## Entry decision

Read only the minimum existing context needed, then decide whether the request is genuinely project bootstrap work.

- If it is project bootstrap work: read `CORE_SKILL.md` and follow its workflow to produce the three formal files.
- If it is not project bootstrap work: do not restart project planning and do not generate the three files. Briefly state that this Skill does not apply, then move to the appropriate implementation, debugging, testing, or release workflow.

Do not activate this Skill merely because the user mentions “software,” “project,” or “AI.”

## Completion handoff

After `PROJECT_BRIEF.md`, `PROJECT_PLAN.md`, and `AI_PROJECT_RULES.md` are complete:

- this Skill ends immediately;
- later development carries and reads only those three files as needed;
- normal implementation, debugging, testing, and release work must not keep loading this Skill;
- later workflows must not redefine confirmed project goals unless the user explicitly approves the change.

This entry file adds only scope, exit, and handoff rules. It does not change the existing three-file pipeline or create a fourth formal file.

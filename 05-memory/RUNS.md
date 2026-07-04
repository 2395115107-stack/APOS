# Runs

## 目标

`RUNS.md` 记录 APOS 每次实际运行任务的过程。

它解决的问题：

- 做过什么任务
- 用了哪个 workflow
- 哪些 agent 参与
- 用了哪些 skills
- review / test 是否通过
- 修正了几轮
- 最终状态是什么

## 记录规则

每跑一次任务，就新增一条 run。

Run 不是复盘文章，而是 agent-readable log。它应该短、结构化、可追踪。

## Run 模板

```text
## RUN-{YYYYMMDD}-{序号}: {任务标题}

Date: {日期}
Status: PASS / FAIL / BLOCKED / PARTIAL
Workflow: {workflow 文件}
Owner: {主 owner}
Agents: planner, architect, designer, frontend, backend, reviewer, tester
Skills: {使用过的 skill；未使用则写 none}
Inputs: {输入文件}
Outputs: {输出文件}
Review: PASS / FAIL / SKIPPED
Test: PASS / FAIL / SKIPPED
Fix Rounds: {次数}
Writeback: {回写文件}

### 结果

{一句话说明结果}

### 失败或风险

- {如无，写 none}

### 下一步

- {如无，写 none}
```

---

## RUN-20260704-001: APOS 最小可运行系统补齐

Date: 2026-07-04
Status: PASS
Workflow: manual / new-feature-like
Owner: planner
Agents: planner
Skills: web-access
Inputs: APOS.md, APOS-SCHEDULING.md, 01-core/AGENTS.md, 08-agents/*, frontier references
Outputs: 02-product/*, 03-design/DESIGN_SYSTEM.md, 04-development/TECH_STACK.md, 05-memory/*, 06-references/*, 07-workflows/*
Review: SELF-CHECK
Test: FILE-CHECK
Fix Rounds: 1
Writeback: 02-product/TASKS.md, 05-memory/DECISIONS.md, 05-memory/LESSONS.md, 05-memory/PATTERNS.md, 05-memory/EVOLUTION.md

### 结果

APOS 已从目录方案进入最小可运行、自进化的文档系统。

### 失败或风险

- 还没有自动化机械检查
- 还没有正式 `review.md` / `hotfix.md` / `initialize.md`
- 还没有 Agent-Computer Interface 规范

### 下一步

- 补 `05-memory/EVALS.md`
- 补 `07-workflows/evaluation.md`
- 后续补 `04-development/AGENT_INTERFACE.md`

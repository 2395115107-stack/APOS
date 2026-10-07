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

---

## RUN-20261007-001: v1.1 收口——补齐常用 workflow 与 agent 接口

Date: 2026-10-07
Status: PASS
Workflow: memory-review-like / documentation
Owner: planner
Agents: planner, reviewer（自检）, architect（接口规范）, tester（文件检查）
Skills: web-access, web-search
Inputs: frontier-agent-systems-gap-analysis.md, APOS-SCHEDULING.md, 2026 年 agent 工程文献（Anthropic / arXiv / GitHub Spec Kit）
Outputs: 04-development/AGENT_INTERFACE.md, 04-development/PERMISSIONS.md, 07-workflows/initialize.md, 07-workflows/review.md, 07-workflows/hotfix.md, 07-workflows/release.md, 07-workflows/redesign.md, 06-references/engineering/agentic-engineering-2026-update.md
Review: SELF-CHECK（引用一致性、字段完整性逐文件核对）
Test: FILE-CHECK（新增文件存在、索引更新、无断裂引用）
Fix Rounds: 1
Writeback: README.md, 02-product/TASKS.md, 02-product/ROADMAP.md, 06-references/README.md, 07-workflows/README.md, 07-workflows/loop.md, 05-memory/*

### 结果

APOS v1.1 完成：九大 workflow 齐备，agent 接口与权限模型建立，2026 年文献落地为接口规范。仓库转为 public。

### 失败或风险

- 新 workflow 尚未在真实项目中运行过，可用性待实际任务验证
- 机械检查仍缺失，文档一致性靠人工核对

### 下一步

- 补 `09-tools/` 机械检查脚本
- 在真实项目中跑一轮完整 loop

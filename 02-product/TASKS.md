# Tasks

## 状态说明

- `TODO`：尚未开始
- `IN_PROGRESS`：进行中
- `REVIEW`：等待 review
- `TEST`：等待测试
- `FIXING`：修正中
- `DONE`：完成
- `BLOCKED`：阻塞

---

## 当前任务

### [DONE] 建立 APOS 目录方案

Owner: planner
Next: none
Inputs: 用户整理的 APOS v1.0 / v2 结构
Outputs: APOS.md
Skills: none
Writeback: 05-memory/DECISIONS.md

### [DONE] 建立调度关系

Owner: planner
Next: none
Inputs: APOS.md, 多智能体协同笔记, dg-agent 样例
Outputs: APOS-SCHEDULING.md
Skills: none
Writeback: 05-memory/DECISIONS.md

### [DONE] 补全 agents

Owner: planner
Next: none
Inputs: APOS-SCHEDULING.md
Outputs: 08-agents/*
Skills: none
Writeback: 05-memory/PATTERNS.md

### [DONE] 补全 AGENTS 总规则和 new-feature workflow

Owner: planner
Next: none
Inputs: APOS-SCHEDULING.md, 08-agents/*
Outputs: 01-core/AGENTS.md, 07-workflows/new-feature.md
Skills: none
Writeback: 05-memory/PATTERNS.md

### [DONE] 补齐最小可运行入口和自进化文件

Owner: planner
Next: reviewer / tester
Inputs: APOS.md, APOS-SCHEDULING.md, 01-core/AGENTS.md, 07-workflows/new-feature.md, 08-agents/*
Outputs: 02-product/*, 03-design/DESIGN_SYSTEM.md, 04-development/TECH_STACK.md, 05-memory/*
Skills: none
Writeback: 05-memory/DECISIONS.md, 05-memory/LESSONS.md

---

## 下一批建议任务

### [TODO] 补全 initialize workflow

Owner: planner
Next: architect / designer / frontend / backend
Inputs: 01-core/AGENTS.md, 07-workflows/new-feature.md
Outputs: 07-workflows/initialize.md
Skills: none
Writeback: 05-memory/PATTERNS.md

### [TODO] 补全 review workflow

Owner: reviewer
Next: tester / frontend / backend
Inputs: 08-agents/reviewer.md, 08-agents/tester.md
Outputs: 07-workflows/review.md
Skills: none
Writeback: 05-memory/PATTERNS.md

### [TODO] 补全 hotfix workflow

Owner: planner
Next: frontend / backend / reviewer / tester
Inputs: 07-workflows/new-feature.md, 08-agents/*
Outputs: 07-workflows/hotfix.md
Skills: none
Writeback: 05-memory/PATTERNS.md


### [DONE] 吸收 OpenAI Harness Engineering 参考

Owner: planner
Next: memory-review
Inputs: https://openai.com/index/harness-engineering/
Outputs: 06-references/engineering/openai-harness-engineering.md, 07-workflows/memory-review.md
Skills: web-access
Writeback: 05-memory/DECISIONS.md, 05-memory/PATTERNS.md, 05-memory/LESSONS.md, 05-memory/EVOLUTION.md

### [DONE] 形成前沿 agent systems 缺口分析

Owner: planner
Next: architect / reviewer
Inputs: OpenAI Harness Engineering, Anthropic Building Effective Agents, SWE-agent, SWE-rebench
Outputs: 06-references/engineering/frontier-agent-systems-gap-analysis.md
Skills: web-access
Writeback: 05-memory/DECISIONS.md, 05-memory/PATTERNS.md, 05-memory/EVOLUTION.md

### [TODO] 补 Agent-Computer Interface 规范

Owner: architect
Next: frontend / backend / reviewer
Inputs: 06-references/engineering/frontier-agent-systems-gap-analysis.md
Outputs: 04-development/AGENT_INTERFACE.md
Skills: none
Writeback: 05-memory/PATTERNS.md

### [DONE] 补运行日志和评估入口

Owner: reviewer
Next: tester / planner
Inputs: 06-references/engineering/frontier-agent-systems-gap-analysis.md
Outputs: 05-memory/RUNS.md, 05-memory/EVALS.md
Skills: none
Writeback: 05-memory/EVOLUTION.md


### [DONE] 添加项目使用说明

Owner: planner
Next: none
Inputs: 01-core/README.md, 02-product/*, 07-workflows/*, 08-agents/*
Outputs: README.md, 01-core/README.md
Skills: none
Writeback: 02-product/TASKS.md

### [DONE] 添加小白使用指南

Owner: planner
Next: none
Inputs: README.md, 01-core/README.md
Outputs: QUICKSTART.md, README.md
Skills: none
Writeback: 02-product/TASKS.md

### [DONE] 吸收 Loop Engineering 参考并补外层闭环

Owner: planner
Next: memory-review
Inputs: https://muximxc.github.io/loop-engineering-guide/, https://arxiv.org/abs/2607.00038
Outputs: 06-references/engineering/loop-engineering-guide.md, 07-workflows/loop.md
Skills: web-access
Writeback: README.md, 06-references/README.md, 07-workflows/README.md, 05-memory/DECISIONS.md, 05-memory/PATTERNS.md, 05-memory/EVOLUTION.md

# Requirements

## 当前需求

让 APOS 从“目录和规则设计”进入“可以真正运行”的状态。

## 用户目标

用户希望 APOS 能作为自己的 AI 产品开发系统使用：

- 能从一个新需求开始
- 能选择 workflow
- 能调度对应 agents
- 能记录任务状态
- 能 review / test
- 能把经验和决策回写到 memory
- 能随着使用不断自进化

## 成功标准

本轮完成后，APOS 应满足：

- `01-core/AGENTS.md` 存在，并定义所有 agent 的总规则
- `02-product/` 有产品、需求、任务、路线图入口
- `03-design/DESIGN_SYSTEM.md` 有最小设计约束
- `04-development/TECH_STACK.md` 有最小技术约束
- `05-memory/` 有决策、经验、模式、演进记录入口
- `07-workflows/new-feature.md` 能指导一次新功能流程
- `08-agents/` 每个 agent 都有职责、skills 路由和输出格式

## 范围

本轮做：

- 补齐 APOS 启动所需的最小文档
- 补齐自进化所需的 memory 文件
- 同步调度关系中的状态模板和自进化闭环

本轮不做：

- 具体业务产品代码
- 具体前端页面实现
- 完整参考库内容
- 所有 workflow 的完整版

## 验收方式

- 文件结构完整
- 关键文档存在
- 新功能流程能从 `REQUIREMENTS.md` 进入，从 `TASKS.md` 跟踪，从 `05-memory/` 回写
- 文档之间没有明显断链

## 当前状态

Status: DONE
Owner: planner
Next: next task
Inputs: APOS.md, APOS-SCHEDULING.md, 01-core/AGENTS.md, 08-agents/*
Outputs: 最小可运行 APOS 文档系统
Skills: none
Writeback: 02-product/TASKS.md, 05-memory/DECISIONS.md, 05-memory/LESSONS.md


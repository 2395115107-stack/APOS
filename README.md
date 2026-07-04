# APOS

APOS 是一个面向 AI 产品开发的本地协作系统。

它不是 GitHub 模板，而是一套让 AI 和人一起长期开发产品的操作系统：用产品文档定义目标，用 workflow 调度任务，用 agents 分工执行，用 memory 记录决策、经验和评估结果。

## 你应该从哪里开始

最短路径：

1. 写需求：`02-product/REQUIREMENTS.md`
2. 建任务：`02-product/TASKS.md`
3. 选流程：`07-workflows/new-feature.md`
4. 调角色：`08-agents/`
5. 做验证：`07-workflows/evaluation.md`
6. 写回忆：`05-memory/`

一次任务的闭环是：

```text
REQUIREMENTS
  -> TASKS
  -> workflow
  -> agents
  -> review / test
  -> RUNS / EVALS
  -> memory
  -> product update
```

## 第一次使用

### 1. 写清当前需求

打开：`02-product/REQUIREMENTS.md`

写清：

- 要做什么
- 给谁用
- 为什么要做
- 做到什么算成功
- 本轮不做什么

### 2. 在任务文件里建任务

打开：`02-product/TASKS.md`

新增：

```text
### [TODO] 任务标题

Owner: planner
Next: planner
Inputs: 02-product/REQUIREMENTS.md
Outputs: 待定
Skills: none
Writeback: 02-product/TASKS.md, 05-memory/*
```

### 3. 使用 new-feature workflow

打开：`07-workflows/new-feature.md`

按流程推进：

```text
planner
  -> architect / designer（按需）
  -> frontend / backend
  -> reviewer
  -> tester
  -> memory / product writeback
```

### 4. 记录运行和评估

每跑完一轮，更新：

- `05-memory/RUNS.md`：记录发生了什么
- `05-memory/EVALS.md`：判断做得怎么样
- `05-memory/LESSONS.md`：记录踩坑
- `05-memory/DECISIONS.md`：记录关键决策
- `05-memory/PATTERNS.md`：沉淀可复用模式
- `05-memory/EVOLUTION.md`：记录 APOS 自身变化

## 你可以这样对 AI 下指令

### 跑一个新功能

```text
使用 APOS，按 new-feature workflow 推进这个需求：
{你的需求}
```

### 做评审

```text
使用 APOS，按 reviewer 角色 review 当前改动，并决定是否需要专项 tester。
```

### 做一次评估

```text
使用 APOS，按 evaluation workflow 评估最近一次任务，并更新 RUNS / EVALS。
```

### 做自进化整理

```text
使用 APOS，按 memory-review workflow 整理 memory，清理过期经验，升级稳定 pattern。
```

## 核心目录

```text
01-core/          总规则、理念、使用入口
02-product/       产品定义、需求、任务、路线图
03-design/        设计系统
04-development/   技术栈和工程约束
05-memory/        决策、经验、模式、运行和评估
06-references/    外部参考
07-workflows/     工作流
08-agents/        AI 角色
```

## 最重要的规则

- 先明确产品目标，再实现
- 任务必须有 `Owner` 和 `Next`
- 重要判断必须落文件
- tester 默认只读
- skills 是能力，不是最高规则
- review / test 失败必须回写 memory
- 完成任务后必须更新 `RUNS.md` 和 `EVALS.md`

## 当前状态

APOS 已具备最小可运行闭环：

- 产品入口已建立
- 新功能 workflow 已建立
- agents 已补齐
- memory 已补齐
- evaluation 已补齐
- 已发布到 GitHub

下一步建议：

- 补 `07-workflows/initialize.md`
- 补 `07-workflows/review.md`
- 补 `07-workflows/hotfix.md`
- 补 `04-development/AGENT_INTERFACE.md`

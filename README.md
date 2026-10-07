# APOS

APOS 是一个面向 AI 产品开发的本地协作系统。

第一次使用请先看：[APOS 小白使用指南](QUICKSTART.md)

它不是 GitHub 模板，而是一套让 AI 和人一起长期开发产品的操作系统：用产品文档定义目标，用 workflow 调度任务，用 agents 分工执行，用 memory 记录决策、经验和评估结果。

## 你应该从哪里开始

最短路径：

1. 写需求：`02-product/REQUIREMENTS.md`
2. 建任务：`02-product/TASKS.md`
3. 判断是否需要闭环：`07-workflows/loop.md`
4. 选流程：`07-workflows/new-feature.md`
5. 调角色：`08-agents/`
6. 做验证：`07-workflows/evaluation.md`
7. 写回忆：`05-memory/`

一次任务的闭环是：

```text
REQUIREMENTS
  -> TASKS
  -> loop
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

### 3. 使用 loop / new-feature workflow

打开：`07-workflows/loop.md` 判断是否需要多轮闭环。

如果只是一次性新功能，直接打开：`07-workflows/new-feature.md`

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

### 跑一个闭环任务

```text
使用 APOS，按 loop workflow 推进这个任务：
{你的任务}

要求：
- 判断是否值得 loop
- 明确成功标准和终态
- 执行后验证
- 更新 RUNS / EVALS / memory
```

### 跑一个紧急修复

```text
使用 APOS，按 hotfix workflow 处理这个线上问题：
{故障现象}

要求：
- 先止血再治本，最小 diff
- 快速验证后恢复
- 24 小时内补全 review 和 memory 回写
```

### 做发布检查

```text
使用 APOS，按 release workflow 检查并发布这个版本。
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

APOS v1.1 已具备完整工作流覆盖：

- 产品入口已建立
- 十大 workflow 已补齐：initialize / new-feature / redesign / review / parallel-review / hotfix / release / loop / evaluation / memory-review
- agents 已补齐
- memory 已补齐
- evaluation 已补齐
- Agent 接口规范已建立：`04-development/AGENT_INTERFACE.md`
- 权限模型已建立：`04-development/PERMISSIONS.md`
- 机械检查已建立：`09-tools/check_docs.py`（必需文件、引用一致性、任务字段）
- 已吸收 2026 年 context / harness / spec-driven 工程共识（见 `06-references/engineering/agentic-engineering-2026-update.md`）

下一步建议：

- 建立任务评估集与回归样例库
- 在真实项目中跑一轮完整 loop，回写 RUNS / EVALS

# Memory Review Workflow

## 目标

`memory-review.md` 用于让 APOS 定期自检和自进化。

它吸收 OpenAI harness engineering 中的两个关键原则：

- repository knowledge is the system of record
- entropy and garbage collection

## 触发时机

- 完成一个新功能后
- review / test 多次失败后
- agent 重复犯同类错误时
- workflow 或 agent 职责发生变化后
- 每完成一批任务后做一次轻量整理

## 输入文件

- `01-core/AGENTS.md`
- `02-product/TASKS.md`
- `05-memory/DECISIONS.md`
- `05-memory/LESSONS.md`
- `05-memory/PATTERNS.md`
- `05-memory/EVOLUTION.md`
- 最近相关 workflow 和 agent 文件

## Step 1: 检查任务闭环

Owner: reviewer

检查：

- 已完成任务是否更新 `TASKS.md`
- 失败原因是否进入 `LESSONS.md`
- 长期决策是否进入 `DECISIONS.md`
- 可复用模式是否进入 `PATTERNS.md`
- 系统变化是否进入 `EVOLUTION.md`

输出：

```text
Owner: reviewer
Next: planner
Outputs: memory review findings
Skills: none
Writeback: 05-memory/LESSONS.md
```

## Step 2: 清理过期信息

Owner: planner

检查：

- 是否有过期规则
- 是否有重复规则
- 是否有只适用于一次任务的经验混入长期 memory
- 是否有文档和当前结构不一致

处理方式：

- 过期：标记或移除
- 重复：合并
- 太细：提升为通用经验，或移出长期 memory
- 冲突：写入 `DECISIONS.md` 等待判断

## Step 3: 固化好模式

Owner: planner / reviewer

如果某个经验重复出现并被验证有效，应提升为 pattern。

写入：

- `05-memory/PATTERNS.md`

## Step 4: 更新系统演进

Owner: planner

如果本轮让 APOS 的能力发生变化，写入：

- `05-memory/EVOLUTION.md`

## 质量门槛

memory review 不能只总结感受。

必须至少输出一种结果：

- 删除或标记过期内容
- 新增 lesson
- 新增 pattern
- 新增 decision
- 新增 evolution 记录
- 明确说明本轮无变化

## 输出格式

```text
Memory Review 完成
Owner: planner / reviewer
Next: none / next workflow
Outputs: 更新过的 memory 文件
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/*
```

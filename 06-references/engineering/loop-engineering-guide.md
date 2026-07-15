# Loop Engineering Guide

Source: https://muximxc.github.io/loop-engineering-guide/

Related paper: https://arxiv.org/abs/2607.00038

## 一句话吸收

Loop Engineering 的核心不是“写更长的提示词”，而是设计一个可重复运行的闭环：触发、目标、执行、验证、停止、记忆。

对 APOS 来说，这个思想非常适合：APOS 已经有 `workflow`、`agents`、`memory` 和 `evaluation`，下一步应把它们组织成可复用的 loop specification。

## 关键观点

### 1. Loop 不是普通循环

这里的 loop 不是代码里的 `while`，也不是 agent 内部的 observe / act 循环。

它是外部设计出来的任务规格：

```text
Trigger
  -> Goal
  -> Execution
  -> Verification
  -> Terminal State
  -> Memory
```

### 2. 检查比提示词更重要

一个 loop 的价值不在于 prompt 写得多漂亮，而在于它如何判断“完成了”。

APOS 应优先设计验证：

- deterministic check：命令、测试、schema、diff
- rule check：规范、lint、约束
- field check：真实运行、用户反馈、部署结果
- judge check：rubric / reviewer / model judge
- human check：人类最终确认

### 3. 只有反馈会改变下一步，才值得做 loop

如果任务只是定时运行一次，不根据结果改变下一步，那只是 scheduled prompt，不是 loop。

APOS 应在每次任务前判断：

- 上一轮结果会不会影响下一轮动作？
- 验证失败后是否有明确修复路径？
- memory 是否会改变之后的执行？

如果答案是否定的，就用一次性 workflow，不要强行 loop。

### 4. 必须有命名终态

loop 不能因为“跑累了”就算成功。

APOS 应固定终态：

- `SUCCESS`：目标达成且验证通过
- `NO_OP`：检查后无需行动
- `BLOCKED`：缺少输入、权限或外部条件
- `STALLED`：多轮无实质进展
- `EXHAUSTED`：预算、时间或轮次耗尽

### 5. Memory 要落盘

loop 的记忆不能只留在对话里。

APOS 应继续把运行结果写入：

- `05-memory/RUNS.md`
- `05-memory/EVALS.md`
- `05-memory/LESSONS.md`
- `05-memory/PATTERNS.md`
- `05-memory/EVOLUTION.md`

## 对 APOS 的改造建议

### 立即采用

- 新增 `07-workflows/loop.md`，作为所有重复任务的外层调度。
- 在 evaluation 中明确终态，而不只写 PASS / FAIL。
- 在每次 workflow 前判断任务是否真的 loopable。

### 暂不采用

- 不马上做自动定时触发，避免成本和误触发。
- 不把 model judge 当作唯一验证，避免自我奖励和虚假通过。
- 不把所有任务都改成 loop，简单任务仍可一次性完成。

## APOS 映射

```text
Trigger         -> 用户指令 / TASKS.md / workflow 入口
Goal            -> REQUIREMENTS.md / TASKS.md 成功标准
Execution       -> 07-workflows/* + 08-agents/*
Verification    -> reviewer / tester / evaluation.md
Terminal State  -> SUCCESS / NO_OP / BLOCKED / STALLED / EXHAUSTED
Memory          -> 05-memory/*
```

## 结论

APOS 现在不只是“有流程”，而应该升级为“有闭环”。

workflow 负责做事，loop 负责决定：

- 什么时候开始
- 怎样判断完成
- 失败后是否再来一轮
- 什么时候停
- 哪些东西要写回 memory

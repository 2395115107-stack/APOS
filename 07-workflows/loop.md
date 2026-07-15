# Loop Workflow

## 目标

`loop.md` 是 APOS 的外层闭环调度流程。

它不替代 `new-feature.md`、`evaluation.md` 或 `memory-review.md`，而是把它们组织成一次可重复、可验证、可停止、可记忆的运行。

## 什么时候使用

使用 loop 的前提：

- 任务需要多轮推进
- 上一轮反馈会改变下一轮动作
- 有明确验证方式
- 有明确停止条件
- 需要写回 memory 以影响未来执行

如果任务只是一次性编辑或说明，不必使用 loop。

## Loop 规格

每个 loop 必须先写清：

```text
Trigger: 谁或什么触发本轮
Goal: 本轮要达成什么
Workflow: 使用哪个 workflow
Agents: 参与哪些 agents
Verification: 如何验证
Terminal State: 如何判断停止
Memory: 写回哪些文件
Budget: 最大轮次 / 时间 / 成本
```

## Step 1: 判断是否值得 Loop

Owner: planner

先回答：

- 反馈是否会改变下一步？
- 验证失败后是否有修复路径？
- memory 是否会影响未来同类任务？

如果三个问题大多是否定，转为一次性 workflow。

## Step 2: 设定目标和终态

Owner: planner / reviewer

目标必须可验证。终态只能是：

- `SUCCESS`：目标完成，验证通过
- `NO_OP`：检查后无需行动
- `BLOCKED`：缺少输入、权限或外部条件
- `STALLED`：连续多轮没有实质进展
- `EXHAUSTED`：轮次、时间或成本用尽

禁止把 `BLOCKED`、`STALLED` 或 `EXHAUSTED` 写成成功。

## Step 3: 选择内部 Workflow

Owner: planner

按任务类型选择：

- 新需求：`new-feature.md`
- 质量判断：`evaluation.md`
- 系统整理：`memory-review.md`
- 评审修复：未来使用 `review.md`
- 紧急修复：未来使用 `hotfix.md`

## Step 4: 执行与验证

Owner: workflow owner / reviewer / tester

执行完成后，按验证强度从高到低选择：

- L1：确定性检查，例如命令退出码、测试、schema
- L2：规则检查，例如 lint、格式、文档字段完整性
- L3：真实反馈，例如运行结果、部署结果、用户反馈
- L4：rubric / model judge
- L5：人工确认

优先使用 L1 / L2。使用 L4 时，生产者不能直接批准自己的结果。

## Step 5: 决定下一轮

Owner: reviewer / planner

根据验证结果决定：

- 通过：写 `SUCCESS`，进入 memory
- 无需行动：写 `NO_OP`，记录原因
- 失败但可修：回到对应 workflow
- 缺少输入：写 `BLOCKED`
- 多轮无进展：写 `STALLED`
- 超过预算：写 `EXHAUSTED`

## Step 6: 写回 Memory

Owner: planner / reviewer

每个 loop 结束必须更新：

- `05-memory/RUNS.md`
- `05-memory/EVALS.md`

如有系统性收获，再更新：

- `05-memory/LESSONS.md`
- `05-memory/PATTERNS.md`
- `05-memory/DECISIONS.md`
- `05-memory/EVOLUTION.md`

## 输出格式

```text
Loop 完成
Owner: planner / reviewer
Next: {next agent or none}
Trigger: {触发来源}
Goal: {目标}
Workflow: {使用的 workflow}
Terminal State: SUCCESS / NO_OP / BLOCKED / STALLED / EXHAUSTED
Verification: {L1-L5 + 证据}
Outputs: {产物}
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/RUNS.md, 05-memory/EVALS.md, ...
```

## 反模式

- 没有验证，只靠 agent 自己说完成
- 没有停止条件，一直循环
- 失败、阻塞或耗尽预算也写成功
- 所有任务都强行 loop
- memory 只留在对话里，不落文件

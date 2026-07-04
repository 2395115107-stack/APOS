# Evaluation Workflow

## 目标

`evaluation.md` 用于评估 APOS 的每次任务运行质量。

它回答的问题不是“有没有做完”，而是：

- 是否做对了
- 是否按正确流程做
- 是否由正确 agent 做
- 是否完成验证
- 是否回写 memory
- 是否推动系统进化

## 触发时机

- 每次 `new-feature.md` 完成后
- 每次 `memory-review.md` 完成后
- 任务失败或阻塞后
- 一批任务结束后

## 输入文件

- `02-product/TASKS.md`
- `05-memory/RUNS.md`
- `05-memory/EVALS.md`
- 当前任务相关 workflow
- 当前任务相关 agent 输出
- review / test 报告

## Step 1: 记录 Run

Owner: planner / reviewer

在 `05-memory/RUNS.md` 中记录：

- 任务标题
- workflow
- agents
- skills
- outputs
- review / test 状态
- fix rounds
- writeback

## Step 2: 评估结果

Owner: reviewer / tester

在 `05-memory/EVALS.md` 中按 5 个维度评估：

- Product Fit
- Workflow Fit
- Agent Fit
- Memory Fit
- Verification Fit

## Step 3: 失败分类

Owner: reviewer

如果失败，至少归类到一个失败来源：

- `REQ`
- `PLAN`
- `ARCH`
- `DESIGN`
- `IMPL`
- `REVIEW`
- `TEST`
- `MEMORY`
- `DOCS`
- `TOOLS`

## Step 4: 生成改进任务

Owner: planner

如果评估发现系统缺陷，需要写入 `02-product/TASKS.md`。

例如：

- workflow 不清 → 修改 workflow
- agent 越权 → 修改 agent 文档
- 经验未回写 → 修改 memory-review 流程
- 验证不足 → 增加 tester 或检查项

## 输出格式

```text
Evaluation 完成
Owner: reviewer / tester
Next: planner / memory-review / none
Outputs: 05-memory/RUNS.md, 05-memory/EVALS.md
Skills: {使用过的 skill；未使用则写 none}
Writeback: 02-product/TASKS.md, 05-memory/LESSONS.md, 05-memory/PATTERNS.md
```

## 质量门槛

一次 evaluation 至少要给出：

- PASS / FAIL / PARTIAL
- 失败分类或 none
- 5 个维度的结果
- 是否需要新增改进任务

如果只写“整体还可以”，不算完成评估。

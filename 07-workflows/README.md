# Workflows

## 说明

`07-workflows/` 是 APOS 的调度中心。

workflow 决定：

- 当前任务属于哪类流程
- 应该按什么顺序执行
- 哪些 agent 参与
- 输入、输出和回写文件是什么
- review / test 如何收口

## 当前可用流程

- `initialize.md`：项目初始化流程
- `new-feature.md`：新增功能流程
- `redesign.md`：页面或体验重构流程
- `review.md`：代码和产物评审流程
- `parallel-review.md`：大范围改动的并行评审编排
- `hotfix.md`：紧急修复流程
- `release.md`：发布前检查流程
- `loop.md`：外层闭环调度流程
- `evaluation.md`：任务运行质量评估流程
- `memory-review.md`：记忆复盘和文档园艺流程

## 待补流程

- `routing.md`：任务路由分发（缺口分析 P2）
- `evaluator-optimizer.md`：独立编排文件（当前模式已并入 `review.md`，按需再拆）

## 机械检查

文档完整性、引用一致性和任务字段由 `09-tools/check_docs.py` 检查：

```text
python 09-tools/check_docs.py
```

## 按场景选择

```text
项目刚接入         -> initialize.md
日常新功能         -> new-feature.md
页面 / 体验重构    -> redesign.md
一轮实现完成       -> review.md
大改动多维验收     -> parallel-review.md
线上故障           -> hotfix.md
准备发布           -> release.md
多轮闭环任务       -> loop.md
判断做得怎么样     -> evaluation.md
整理经验与文档     -> memory-review.md
```

## 通用输出字段

```text
Owner
Next
Inputs
Outputs
Skills
Writeback
```

## 使用规则

1. 任务先进入 `02-product/TASKS.md`
2. 判断是否需要 `loop.md`
3. 再选择内部 workflow
4. workflow 决定参与 agents
5. agents 执行后回到 workflow 收口
6. loop / evaluation 判断终态
7. 最终回写 `05-memory/` 和 `02-product/`

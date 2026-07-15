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

- `new-feature.md`：新增功能流程
- `loop.md`：外层闭环调度流程
- `evaluation.md`：任务运行质量评估流程
- `memory-review.md`：记忆复盘和文档园艺流程

## 待补流程

- `initialize.md`：初始化项目
- `review.md`：代码和产物评审
- `hotfix.md`：紧急修复
- `redesign.md`：页面或体验重构
- `release.md`：发布前检查

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

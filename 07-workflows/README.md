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
2. 再选择 workflow
3. workflow 决定参与 agents
4. agents 执行后回到 workflow 收口
5. 最终回写 `05-memory/` 和 `02-product/`

# 08-agents

## 说明

这一层定义 APOS 的执行角色。

角色不是越多越好，而是边界越清晰越好。默认主链路使用：

- `planner`
- `architect`
- `designer`
- `frontend`
- `backend`
- `reviewer`
- `tester`

当任务复杂度上升，再按需启用专项 tester：

- `tester-layout`
- `tester-quality`
- `tester-performance`
- `tester-accessibility`

## 使用顺序

1. 由 `planner` 明确目标、任务、脚手架和交接文件
2. 按需进入 `architect` / `designer`
3. 由 `frontend` / `backend` 实现
4. 先 `reviewer`，再 `tester`
5. 复杂任务按需追加专项 tester
6. 所有反馈回写 `05-memory/`，必要时同步 `02-product/`

## 共通规则

- 所有角色都必须先读必要文件，再行动
- 角色可以按任务类型启用相关 skills，但本项目文档和现有代码模式优先级更高
- 执行角色输出尽量简短，详细内容落文件
- tester 默认只读，不直接修改代码
- 修正优先走原责任链路
- 发现文档与实现偏离时，必须显式指出

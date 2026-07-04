# APOS

## 如何使用

APOS 是你的 AI 产品开发系统。

最短使用路径：

1. 在 `02-product/REQUIREMENTS.md` 写清当前需求
2. 在 `02-product/TASKS.md` 建立任务状态
3. 选择 `07-workflows/` 中对应流程
4. 按流程调度 `08-agents/` 中的角色
5. 完成后回写 `05-memory/`

## 默认入口

- 总规则：`01-core/AGENTS.md`
- 产品定义：`02-product/PRODUCT.md`
- 当前需求：`02-product/REQUIREMENTS.md`
- 当前任务：`02-product/TASKS.md`
- 新功能流程：`07-workflows/new-feature.md`
- Agent 角色：`08-agents/README.md`
- 记忆库：`05-memory/`

## 一次任务的最小闭环

```text
REQUIREMENTS
  -> TASKS
  -> workflow
  -> agents
  -> review / test
  -> memory
  -> TASKS / REQUIREMENTS update
```

## 使用原则

- 不清楚目标时，先补需求，不急着实现
- 任务必须有 owner 和 next owner
- 重要判断必须落文件
- review / test 失败必须回写经验
- skills 可以使用，但不能覆盖项目文档

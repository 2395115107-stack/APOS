# APOS Core

这里是 APOS 的核心入口。

## 文件说明

- `README.md`：核心层使用入口
- `MANIFESTO.md`：APOS 的理念和判断优先级
- `AGENTS.md`：所有 agent 必须遵守的总规则

## 使用顺序

1. 先读 `MANIFESTO.md`，理解 APOS 为什么存在
2. 再读 `AGENTS.md`，理解所有 agent 的工作规则
3. 回到根目录 `README.md`，按使用说明开始跑任务

## 核心判断

APOS 的工作方式是：

```text
产品目标
  -> workflow
  -> agents
  -> review / test
  -> runs / evals
  -> memory
  -> product update
```

如果不确定下一步做什么，回到：

- `02-product/REQUIREMENTS.md`
- `02-product/TASKS.md`
- `07-workflows/new-feature.md`

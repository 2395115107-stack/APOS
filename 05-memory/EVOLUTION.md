# Evolution

## 记录规则

这里记录 APOS 自身如何演进。

每次系统能力变化，都记录：

- 日期
- 变化
- 原因
- 影响
- 下一步

---

## 2026-07-04：APOS 从目录方案进入最小可运行系统

### 变化

补齐：

- `01-core/AGENTS.md`
- `02-product/*`
- `03-design/DESIGN_SYSTEM.md`
- `04-development/TECH_STACK.md`
- `05-memory/*`
- `07-workflows/new-feature.md`
- `08-agents/*`

### 原因

系统不能只停留在目录和规则，需要能真正从需求进入、由 workflow 调度、由 agent 执行、由 memory 回写。

### 影响

APOS 已具备最小闭环：

```text
PRODUCT / REQUIREMENTS
  -> TASKS
  -> new-feature workflow
  -> agents
  -> review / test
  -> memory
  -> product update
```

### 下一步

- 补 `initialize.md`
- 补 `review.md`
- 补 `hotfix.md`
- 建立定期 memory review 流程

---

## 2026-07-04：吸收 OpenAI Harness Engineering 参考

### 变化

新增：

- `06-references/engineering/openai-harness-engineering.md`
- `07-workflows/memory-review.md`

### 原因

APOS 需要从“文档齐全”进一步走向“agent 可读、可验证、可回收熵”的工程系统。

### 影响

APOS 增加了 memory review / 文档园艺流程，用于定期清理过期经验、升级稳定模式、记录系统演进。

---

## 2026-07-04：完成前沿 agent systems 缺口分析

### 变化

新增：

- `06-references/engineering/frontier-agent-systems-gap-analysis.md`

### 原因

APOS 已有最小运行闭环，但前沿 agent 系统还强调 evaluation loop、agent-computer interface、observability、permissions 和 mechanical checks。

### 影响

下一轮 APOS 应优先补：

- `04-development/AGENT_INTERFACE.md`
- `05-memory/RUNS.md`
- `05-memory/EVALS.md`
- `04-development/PERMISSIONS.md`

---

## 2026-07-04：补齐评估循环

### 变化

新增：

- `05-memory/RUNS.md`
- `05-memory/EVALS.md`
- `07-workflows/evaluation.md`

### 原因

APOS 需要记录每次任务运行质量，不只是记录任务是否完成。

### 影响

APOS 现在具备最小评估循环：

```text
run log
  -> eval result
  -> failure class
  -> improvement task
  -> memory update
```

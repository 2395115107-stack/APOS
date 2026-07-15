# Decisions

## 记录规则

这里记录 APOS 的关键决策。

一条好决策应该包含：

- 背景
- 选项
- 决定
- 原因
- 影响
- 后续检查点

---

## DEC-001：采用数字分层目录

Date: 2026-07-04
Owner: planner
Status: accepted

### 背景

APOS 不是 GitHub 模板，而是 AI 产品开发系统。目录需要帮助人和 AI 按固定顺序理解上下文。

### 决定

采用：

```text
01-core
02-product
03-design
04-development
05-memory
06-references
07-workflows
08-agents
```

### 原因

- 阅读顺序稳定
- 产品优先于实现
- 后续扩展自然
- AI 更容易按层读取

### 影响

所有 workflow 和 agent 都应遵循这个层级关系。

---

## DEC-002：workflow 是调度中心

Date: 2026-07-04
Owner: planner
Status: accepted

### 背景

如果 agent 互相自由调用，长期协作容易失控。

### 决定

由 `07-workflows/` 负责编排，`08-agents/` 负责执行。

### 原因

- 流程稳定
- 角色边界清晰
- 便于 review / test 收口
- 便于记录输入、输出、回写

---

## DEC-003：skills 是能力，不是最高规则

Date: 2026-07-04
Owner: planner
Status: accepted

### 背景

不同 agent 需要借助 skills，但不能让 skill 覆盖项目文档和产品目标。

### 决定

skills 按场景可选，优先级低于 APOS 文档和项目规范。

### 影响

所有 agent 输出中增加 `Skills:` 字段。

---

## DEC-004：memory 是自进化入口

Date: 2026-07-04
Owner: planner
Status: accepted

### 背景

APOS 要真正自进化，不能只记录当前任务结果，还要记录决策、经验、模式和系统变化。

### 决定

`05-memory/` 固定承载：

- `DECISIONS.md`
- `LESSONS.md`
- `PATTERNS.md`
- `EVOLUTION.md`

### 影响

workflow 完成后必须回写 memory。

---

## DEC-005：采用 Harness Engineering 作为 APOS 工程原则

Date: 2026-07-04
Owner: planner
Status: accepted

### 背景

OpenAI 的 harness engineering 文章强调：人的重点从直接写代码转向设计 agent 可工作的环境、工具、约束和反馈回路。

### 决定

APOS 采用 harness engineering 作为工程参考原则。

### 原因

- APOS 本质上也是给 AI agent 使用的开发系统
- agent 需要稳定入口、结构化上下文和可验证反馈
- 自进化需要 memory review 和文档垃圾回收

### 影响

- 新增 `06-references/engineering/openai-harness-engineering.md`
- 新增 `07-workflows/memory-review.md`
- 后续应避免把 `AGENTS.md` 写成百科全书，而应保持为地图和索引

---

## DEC-006：采用 Loop Engineering 作为外层调度原则

Date: 2026-07-15
Owner: planner
Status: accepted

### 背景

APOS 已经具备 workflow、agents、memory 和 evaluation，但如果每次仍靠人手动决定下一步，系统还没有真正形成可重复闭环。

### 决定

新增 `07-workflows/loop.md`，作为 APOS 的外层闭环调度原则。

### 原因

- loop 能明确触发、目标、验证、停止和记忆
- 可以避免 agent 无限制循环或虚假完成
- 可以让 evaluation 和 memory 真正参与下一轮行动

### 影响

复杂任务应先判断是否值得 loop；如果需要多轮推进，必须写清终态和验证方式。

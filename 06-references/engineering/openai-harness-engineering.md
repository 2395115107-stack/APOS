# OpenAI: Harness Engineering

Source: https://openai.com/index/harness-engineering/
Date referenced: 2026-07-04
Type: Engineering reference

## 为什么收录

这篇文章对 APOS 很关键，因为它把“AI 写代码”重新定义成“人设计 harness，agent 在 harness 中执行”。

APOS 要吸收的不是具体工具栈，而是下面这些可迁移原则。

## 核心提炼

### 1. Humans steer, agents execute

人的工作重点从直接写代码，转向：

- 设计环境
- 说明意图
- 提供工具
- 建立反馈回路
- 编码约束

APOS 对应：

- `01-core/AGENTS.md` 定义总规则
- `07-workflows/` 定义流程
- `08-agents/` 定义执行角色
- `05-memory/` 承载反馈和演进

### 2. AGENTS.md 是地图，不是百科全书

不要把所有规则塞进一个巨大的 `AGENTS.md`。

更好的做法是：

- `AGENTS.md` 保持短、稳定、指向性强
- 具体事实放到结构化文档目录
- agent 从小入口进入，再按需展开上下文

APOS 对应：

- `01-core/AGENTS.md` 是总入口
- `02-product/` 是产品事实源
- `03-design/` 是设计事实源
- `04-development/` 是技术事实源
- `05-memory/` 是长期记忆

### 3. Repository knowledge is the system of record

agent 看不到的东西，等于不存在。

所以重要知识不能只在：

- 聊天记录
- 口头共识
- 外部文档
- 一次性 prompt

APOS 对应：

- 产品目标写入 `02-product/`
- 技术决策写入 `05-memory/DECISIONS.md`
- 踩坑经验写入 `05-memory/LESSONS.md`
- 可复用模式写入 `05-memory/PATTERNS.md`

### 4. Plans are first-class artifacts

计划不是临时思考，而是应该版本化、可回看、可更新的工件。

APOS 对应：

- `02-product/TASKS.md` 管任务状态
- `07-workflows/*.md` 管流程
- 复杂任务应额外创建计划文件或任务记录

### 5. Agent legibility is the goal

系统要让 agent 能读懂、验证、修改。

这意味着：

- 目录结构稳定
- 文件命名清楚
- 输入输出格式固定
- 日志、测试、报告可读
- 重要状态可查询

APOS 对应字段：

```text
Owner
Next
Inputs
Outputs
Skills
Writeback
```

### 6. Enforce invariants mechanically

文档本身不够，关键约束应该尽量变成可检查规则。

APOS 当前先用文档约束，后续应逐步加入：

- 文档完整性检查
- 交叉引用检查
- 任务状态检查
- memory 回写检查
- agent 输出格式检查

### 7. Entropy and garbage collection

agent 会复制已有模式，包括坏模式。系统必须定期清理。

APOS 对应：

- `05-memory/EVOLUTION.md` 记录系统能力变化
- `07-workflows/memory-review.md` 定期检查 memory 和文档漂移
- `05-memory/LESSONS.md` 记录坏模式
- `05-memory/PATTERNS.md` 固化好模式

## 对 APOS 的具体优化

### 已吸收

- 建立 `05-memory/` 作为自进化入口
- 所有 agent 输出加入 `Skills`
- workflow 强制写 `Owner / Next / Inputs / Outputs / Writeback`
- `APOS-SCHEDULING.md` 加入自进化检查

### 本次新增

- 将本文沉淀到 `06-references/engineering/`
- 新增 `07-workflows/memory-review.md`
- 在 memory 中记录 harness engineering 原则

## APOS 采用的判断

APOS 不追求“全自动”。

APOS 追求：

```text
人定义目标和判断标准
  -> workflow 编排
  -> agent 执行
  -> review/test 验证
  -> memory 回写
  -> 系统自进化
```

这比单纯增加 agent 数量更重要。

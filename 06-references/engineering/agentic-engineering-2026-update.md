# Agentic Engineering 2026 Update

Date: 2026-10-07
Scope: APOS v1.1 收口

## Sources

- Anthropic, Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic, Writing effective tools for agents—with agents: https://www.anthropic.com/engineering/writing-tools-for-agents
- Anthropic, Building Effective Agents（2026-07 已收录，本次复核）: https://www.anthropic.com/engineering/building-effective-agents
- Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned (arXiv:2603.05344, 2026-03): https://arxiv.org/abs/2603.05344
- MemoHarness: Agent Harnesses That Learn from Experience (2026-07): https://www.alphaxiv.org
- Spec-driven development（GitHub Spec Kit）: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit
- From Code to Contract in the Age of AI Coding Assistants (arXiv:2602.00180): https://arxiv.org/abs/2602.00180
- Microsoft, A Spec-First Approach to AI-Native Engineering: https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering
- 2026 code review / evaluation 实践共识（HackerNoon, dev.to 等社区综述）

## 总判断

2025 下半年到 2026 年，agent 工程共识从 prompt engineering 转向两层：

1. **context engineering**：决定每个步骤让模型看到什么信息
2. **harness engineering**：把模型周围的脚手架（上下文、工具、编排、记忆、控制回路）当作一等工程对象

APOS 的定位（人定义目标 → workflow 编排 → agent 执行 → 验证 → memory 回写）与这层共识一致。本次收口要补的是把这些共识落成可执行接口。

---

## 原则提炼与 APOS 映射

### 1. 最小高信号 token 集

Anthropic：上下文工程的目标是找到最小的高信号 token 集，而不是塞满上下文窗。配套技术：compaction、结构化笔记、sub-agent 上下文隔离。

APOS 映射：

- `04-development/AGENT_INTERFACE.md` 上下文预算与读取约定
- 交接只传状态与路径，详细内容落文件（已有调度原则，本次接口化）

### 2. 工具宁少勿滥，用 agent 迭代工具

Anthropic：agent 的效果上限由工具质量决定；更少的、设计良好的工具胜过一大堆工具；应让 agent 原型、测试并迭代工具本身。

APOS 映射：

- skills 按任务路由，不固定绑定（LESSONS 已有）
- `AGENT_INTERFACE.md` 统一输出块，减少每个 agent 的自由格式成本

### 3. 规格即契约（spec-driven development）

GitHub Spec Kit / arXiv:2602.00180 / Microsoft：当 agent 写越来越多的代码时，规格成为持久事实源，代码是规格的可验证产物；验收标准先行。

APOS 映射：

- `REQUIREMENTS.md` + 成功标准就是 APOS 的 spec
- `initialize.md` 把建立规格入口作为初始化 P0
- `review.md` Step 1 要求评审以需求为锚，不只看 diff

### 4. 确定性检查优先

2026 年 evaluation 实践共识：确定性检查（构建、测试、lint、schema）能以极低成本拦住大多数问题；LLM judge 只用于确定性规则覆盖不到的维度，且生产者不能自评通过。

APOS 映射：

- `review.md` Step 2 把 L1 / L2 检查设为硬性前置
- `release.md` Step 3 要求验证证据链
- 沿用 `loop.md` 的 L1-L5 验证阶梯

### 5. 评审分工：机器管风格，判断管架构

2026 年 code review 共识：风格、语法类问题交给机器；人和强 agent 评审聚焦安全、架构、行为正确性。

APOS 映射：

- `review.md` Step 3 的维度优先级（行为与数据安全先于风格）
- 并行评审拆分（orchestrator-workers）

### 6. Harness 是管理上下文、工具、编排、记忆的外层控制层

MemoHarness（2026-07）等工作把 harness 定义为把基础 LLM 变成可执行 agent 的外层控制层，并探索 harness 从经验中学习。

APOS 映射：

- APOS 本身就是一个 harness：`07-workflows/` 是编排，`05-memory/` 是跨轮记忆，`AGENT_INTERFACE.md` 是接口层
- harness 从经验学习这一步，在 APOS 中由 `memory-review.md` + `EVALS.md` 承担（人工节拍），暂不自动化

---

## 本次落地

基于以上文献，本轮补齐：

- `04-development/AGENT_INTERFACE.md`（缺口分析 Gap 2，P0 收尾）
- `04-development/PERMISSIONS.md`（缺口分析 Gap 7）
- `07-workflows/initialize.md`
- `07-workflows/review.md`
- `07-workflows/hotfix.md`
- `07-workflows/release.md`
- `07-workflows/redesign.md`

至此 ROADMAP v1.1（常用 workflow 补齐）完成，APOS 具备完整工作流覆盖。

---

## 暂不采用

- **observability 驱动的 harness 自动进化**（Agentic Harness Engineering 一类工作）：需要运行时遥测与自动管线，APOS 当前是文档驱动阶段，用 `memory-review` 人工节拍替代。
- **learnable harness controller**（HarnessBridge 一类）：模型层改动，超出文档系统范围。
- **自动定时触发 loop**：沿用 2026-07 判断，避免成本与误触发。

## 结论

2026 年文献没有推翻 APOS 的结构，而是验证了它：文件即记忆、流程先于角色、验证先于生成，这些判断都与主流实践同向。本次收口把"共识"变成了"接口"。

文献结论会过时，references 必须带收录日期，落地前以当下验证为准。

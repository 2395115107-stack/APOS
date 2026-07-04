# APOS v1.0 目录方案

## 核心定位

> **这是你的开发系统，不是一个 GitHub 模板。**

APOS 的目标不是提供一套“好看的模板目录”，而是为 AI 产品开发提供一套可持续协作的工作系统。

它需要同时服务：

- 人类开发者的阅读与决策
- AI Agent 的理解与执行
- 产品、设计、开发、测试的跨角色协作

---

## 设计判断

这次目录设计，真正要解决的不是“文件放哪里”，而是下面三个问题：

1. 产品信息是否比工程细节更靠前
2. AI 是否能按固定顺序理解项目上下文
3. 后续扩展时，结构是否还能稳定生长

基于这三个标准，**V2 比 V1 更适合作为 APOS v1.0 正式结构**。

结合你补充的“多智能体协同 / 长时工作”笔记，APOS 还应该额外吸收 4 个长期有效的判断：

1. **文件即记忆**：重要状态、结论、经验必须落文件，不能只留在对话里
2. **隔离即常态**：每个 Agent 默认只看当前任务所需上下文，不假设全局都已知
3. **流程先于角色**：真正的调度中心应该是 workflow，而不是让 agent 自由互相调用
4. **闭环比产出更重要**：任务完成不是结束，经验回写和产品回写才构成系统成长

这 4 条不会改变 APOS 的目录结构，但会强化 APOS 的运行方式。

再结合你给的 `dg-planner / dg-slide-dev / dg-slide-tester-*` 这组样例，APOS 的调度设计还应吸收 3 个更细的工程判断：

1. **计划层要前置产出“执行脚手架”**：planner 不只拆任务，还应准备基础设施、任务表、设计/认知指引
2. **测试层要按维度拆分**：布局、审美、动画、性能、可访问性等可以拆成独立 tester，而不是永远只有一个总 tester
3. **交接输出要极简、结构化**：执行 agent 的返回只保留状态与路径，详细内容落文件，避免主上下文被污染

这 3 条会直接影响 APOS 后续的 workflow 和 agent 模板设计。

---

## 推荐方案：V2

```text
APOS/
│
├── 01-core/
│   ├── README.md
│   ├── MANIFESTO.md
│   └── AGENTS.md
│
├── 02-product/
│   ├── PRODUCT.md
│   ├── ROADMAP.md
│   ├── REQUIREMENTS.md
│   └── TASKS.md
│
├── 03-design/
│   └── DESIGN_SYSTEM.md
│
├── 04-development/
│   └── TECH_STACK.md
│
├── 05-memory/
│   ├── LESSONS.md
│   ├── EVOLUTION.md
│   ├── DECISIONS.md
│   └── PATTERNS.md
│
├── 06-references/
│
├── 07-workflows/
│
└── 08-agents/
```

---

## 为什么推荐 V2

### 1. 阅读顺序天然固定

数字前缀让人和 AI 都按同一顺序读取：

`01-core -> 02-product -> 03-design -> 04-development -> 05-memory -> 06-references -> 07-workflows -> 08-agents`

这能显著减少“先看哪里”的歧义。

### 2. 更符合 AI 产品开发逻辑

这套结构把“产品定义”放在“开发实现”之前，符合真实工作流：

- 先明确理念与规则
- 再定义产品
- 再沉淀设计与技术
- 最后进入执行与迭代

这比传统工程模板更贴近 AI 产品团队的工作方式。

### 3. 扩展性更强

后续如果需要新增目录，可以自然扩展：

- `09-tools/`
- `10-examples/`
- `11-assets/`

不会破坏整体认知顺序。

---

## 七层模型

```text
① Core（理念与规则）
        │
② Product（产品定义）
        │
③ Design（设计语言）
        │
④ Development（技术实现）
        │
⑤ Memory（经验记忆）
        │
⑥ References（外部参考）
        │
⑦ Workflows / Agents（流程与执行）
```

这个七层模型在吸收多智能体笔记后，可以进一步理解为三种能力的分层：

- `Core + Product`：定义系统目标与判断标准
- `Workflow + Agents`：负责任务编排与具体执行
- `Memory + References`：负责长期学习与跨轮次复用

也就是说，APOS 不只是“目录分层”，而是“短期执行层”和“长期记忆层”并存的系统。

---

## 各层职责

### 01-core

回答两个问题：

- 我们是谁？
- AI 应该如何工作？

包含：

- `README.md`：如何使用 APOS
- `MANIFESTO.md`：系统理念与价值观
- `AGENTS.md`：AI 协作总规则

### 02-product

回答一个问题：

- 我们要做什么？

包含：

- `PRODUCT.md`：产品定义
- `ROADMAP.md`：阶段目标
- `REQUIREMENTS.md`：当前需求
- `TASKS.md`：当前执行任务

### 03-design

回答一个问题：

- 产品应该长什么样、遵循什么体验原则？

包含：

- `DESIGN_SYSTEM.md`

### 04-development

回答一个问题：

- 技术上怎么落地？

包含：

- `TECH_STACK.md`

### 05-memory

回答一个问题：

- 我们学到了什么？

包含：

- `LESSONS.md`
- `EVOLUTION.md`
- `DECISIONS.md`
- `PATTERNS.md`

这一层在多智能体协同里尤其关键，因为它不是资料归档层，而是**跨任务、跨 agent 的持久化上下文层**。

建议这样理解四个文件：

- `DECISIONS.md`：记录为什么这样定
- `LESSONS.md`：记录踩坑和修正
- `PATTERNS.md`：记录哪些方法可以复用
- `EVOLUTION.md`：记录系统能力如何变化

### 06-references

回答一个问题：

- 我们在向谁学习？

建议后续按主题继续细分，例如：

- `design/`
- `products/`
- `engineering/`

### 07-workflows

回答一个问题：

- 关键任务应该按什么流程推进？

建议后续放入：

- `initialize.md`
- `new-feature.md`
- `redesign.md`
- `review.md`
- `release.md`
- `hotfix.md`

### 08-agents

回答一个问题：

- 不同 AI 角色分别负责什么？

建议后续放入：

- `planner.md`
- `architect.md`
- `designer.md`
- `frontend.md`
- `backend.md`
- `reviewer.md`
- `tester.md`

后续如果测试体系变复杂，也可以从一个 `tester.md` 继续细分为多个维度型 tester，例如：

- `tester-layout.md`
- `tester-quality.md`
- `tester-performance.md`
- `tester-accessibility.md`

---

## V1 与 V2 的区别

### V1 的优点

- 更接近传统目录树
- 一眼能看到所有能力模块
- 对工程师更熟悉

### V1 的问题

- 目录优先级不够明确
- AI 和人都容易横向浏览，而不是纵向理解
- 产品层、流程层、角色层混在同一视觉级别

### V2 的优点

- 顺序更稳定
- 产品导向更强
- 更适合作为“开发操作系统”而不是“模板仓库”

### 结论

如果 APOS 的定位是长期演进的 AI 产品开发系统，**推荐正式采用 V2**。

---

## 建议的下一步

如果要把这套结构真正跑起来，建议按下面顺序补齐内容：

1. 先写 `01-core/AGENTS.md`
2. 再写 `02-product/PRODUCT.md`
3. 然后补 `02-product/REQUIREMENTS.md` 与 `TASKS.md`
4. 再沉淀 `07-workflows/` 和 `08-agents/`
5. 最后持续积累 `05-memory/` 与 `06-references/`
6. 每个 workflow 都要定义“输入文件、输出文件、回写文件”

这样 APOS 才不仅是目录清晰，而是真的具备长期运行能力。

---

## 最终结论

APOS v1.0 推荐采用 **V2 数字分层结构**。

它不是为了“看起来像一个标准仓库”，而是为了让：

- 人更容易协作
- AI 更容易理解
- 产品开发更容易持续推进

这才是 APOS 的核心价值。

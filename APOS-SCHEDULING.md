# APOS 调度关系

## 核心原则

APOS 的调度关系不是“谁权限最大”，而是“谁在当前阶段最接近真实问题”。

所以它遵循 4 个原则：

1. `Product` 决定方向，不直接写实现
2. `Workflow` 负责编排，不长期持有业务决策
3. `Agent` 负责执行，各自只处理本职上下文
4. `Reviewer` 和 `Tester` 负责收口，避免错误直接进入主线

结合你提供的多智能体长时协同笔记，调度层还应再补 4 个运行原则：

1. **文件即记忆**：计划、结论、经验都必须落文件
2. **隔离即常态**：每个执行角色默认只看完成当前任务所需上下文
3. **记录即保险**：关键交接、测试结论、回退原因都必须可追溯
4. **resume 优于重讲**：同一任务的修正应尽量在原执行链路上延续，而不是重新从零解释

结合 `dg-planner / dg-slide-dev / dg-slide-tester-*` 的实践，调度层再补 4 条优化原则：

1. **planner 先铺路再派工**：先产出计划、基础设施、认知/设计指引，再进入逐任务开发
2. **tester 按维度拆分**：复杂项目优先拆成多个窄职责 tester，而不是一个大而全 tester
3. **交接尽量只传状态和路径**：详细内容落文件，主编排上下文只保留必要信号
4. **重测只验证失败项**：回归测试应聚焦上轮问题，避免重复全量审查

这 8 条共同决定了 APOS 的“长时运行稳定性”。

---

## 总体调度结构

```text
01-core
  └── 提供全局规则
        ↓
02-product
  └── 提供目标、需求、优先级
        ↓
07-workflows
  └── 根据任务类型选择执行流程
        ↓
08-agents
  └── 按角色分工执行
        ↓
03-design / 04-development
  └── 提供设计与技术约束
        ↓
05-memory
  └── 沉淀决策、经验、模式
        ↓
02-product
  └── 反哺下一轮产品迭代
```

这意味着：

- `01-core` 是总规则入口
- `02-product` 是任务入口
- `07-workflows` 是流程入口
- `08-agents` 是执行入口
- `05-memory` 是反馈入口

---

## 分层调度关系

## 1. Core -> 全局约束

`01-core` 不直接参与任务执行，但它决定所有调度的基础规则。

包含：

- `README.md`：告诉人和 AI 怎么进入系统
- `MANIFESTO.md`：定义价值观与判断优先级
- `AGENTS.md`：定义所有 Agent 的共同行为规则

调度职责：

- 为所有流程提供统一原则
- 限制 Agent 的越权行为
- 统一输出格式、协作方式、升级策略

一句话理解：

> `01-core` 不做事，但决定“怎么做事才算对”。

---

## 2. Product -> 任务发起层

`02-product` 是真实需求的来源。

包含：

- `PRODUCT.md`
- `ROADMAP.md`
- `REQUIREMENTS.md`
- `TASKS.md`

调度职责：

- 定义要解决什么问题
- 定义当前阶段优先级
- 把长期目标拆成可执行任务

它触发的不是具体 Agent，而是对应 `workflow`。

一句话理解：

> `Product` 负责发任务，但不直接指挥每个执行角色。

---

## 3. Workflow -> 编排层

`07-workflows` 是 APOS 的真正调度中枢。

它不替代 Agent，而是决定：

- 当前属于哪一类任务
- 应该按什么顺序走
- 需要哪些角色参与
- 什么时候进入 review / test / release
- 哪些文件是输入、输出和回写目标

### 推荐工作流映射

```text
initialize.md
  -> planner
  -> architect
  -> designer
  -> frontend / backend
  -> reviewer
  -> tester

new-feature.md
  -> planner
  -> architect（按需）
  -> designer（按需）
  -> frontend / backend
  -> reviewer
  -> tester

redesign.md
  -> planner
  -> designer
  -> frontend
  -> reviewer
  -> tester

review.md
  -> reviewer
  -> frontend / backend 修复
  -> tester 回归

release.md
  -> reviewer
  -> tester
  -> release checklist

hotfix.md
  -> planner（快速确认问题边界）
  -> backend / frontend
  -> reviewer
  -> tester
```

一句话理解：

> `Workflow` 不产出业务成果，但决定成果如何被稳定产出。

---

## 4. Agents -> 执行层

`08-agents` 是具体干活的角色层。

每个 Agent 都应该只处理自己最擅长的一段问题。

### 推荐角色关系

```text
planner
  -> 负责理解目标、拆分任务、明确范围
  -> 前置产出计划、任务表、执行脚手架、认知/设计指引

architect
  -> 负责技术方案、边界、数据流、模块关系

designer
  -> 负责界面结构、交互、视觉表达

frontend
  -> 负责前端实现与体验还原

backend
  -> 负责服务、数据、接口、权限、稳定性

reviewer
  -> 负责发现风险、回归、规范问题

tester
  -> 负责验证功能、边界、异常路径
  -> 在复杂项目中可继续拆成多个维度 tester
```

---

## Agent 间调度关系

### 主链路

```text
planner
  -> architect / designer
  -> frontend / backend
  -> reviewer
  -> tester
```

这是默认主链路，适合大多数新功能开发。

### 设计驱动链路

```text
planner
  -> designer
  -> frontend
  -> reviewer
  -> tester
```

适合页面重构、体验升级、品牌更新。

### 技术驱动链路

```text
planner
  -> architect
  -> backend / frontend
  -> reviewer
  -> tester
```

适合重构、性能优化、权限模型调整、数据结构调整。

### 紧急修复链路

```text
planner
  -> 直接定位问题
  -> frontend / backend
  -> reviewer
  -> tester
```

适合线上 bug、阻塞缺陷、发布前修复。

### 专项测试链路

```text
planner / reviewer
  -> tester-layout
  -> tester-quality
  -> tester-performance
  -> 汇总回 frontend / backend
```

适合前端体验、设计质量、复杂交互、富媒体内容这类需要分维度验收的任务。

---

## 谁能触发谁

为了避免角色混乱，建议使用下面这套触发关系。

### 一级触发

- `core` 可以约束所有层，但不主动触发执行
- `product` 触发 `workflow`
- `workflow` 触发 `agents`

### 二级触发

- `planner` 可以触发 `architect`、`designer`、`frontend`、`backend`
- `planner` 可以先要求相关角色读取计划、指南、脚手架文件，再进入实现
- `architect` 可以向 `frontend`、`backend` 下发技术约束
- `designer` 可以向 `frontend` 下发界面与交互约束
- `reviewer` 可以把任务退回 `frontend` / `backend` / `designer`
- `reviewer` 或主 workflow 可以按需触发多个专用 tester 并行审查
- `tester` 可以把任务退回 `frontend` / `backend`

### 不建议的触发

- `frontend` 不应直接改写产品目标
- `backend` 不应直接决定设计规范
- `designer` 不应直接覆盖架构决策
- `reviewer` 不应替代 `planner` 做需求定义

一句话理解：

> 能发现问题的人不一定能改方向，能改方向的人也不应该直接跳过流程。

---

## 长时协同补充规则

如果 APOS 要支持多轮次、多 Agent 的长时协同，建议再明确 6 条规则。

### 规则 1：任务必须有持久化状态

每个任务至少要有：

- 当前状态
- 当前 owner
- 下一责任角色
- 相关输入文件
- 相关输出文件
- 回写目标文件

### 规则 2：修正优先走原链路

同一任务如果进入修正循环，优先由原负责角色继续处理，而不是换一个新角色重新理解一遍。

这样可以减少上下文丢失和重复解释成本。

### 规则 3：测试只读、开发可写

测试角色不应直接修改产物，只负责给出 PASS / FAIL 和问题列表。

这样职责边界更清晰，也更适合做回归闭环。

### 规则 4：经验必须回写

只要一个问题被 reviewer 或 tester 打回，就应该沉淀到 `05-memory/LESSONS.md` 或 `DECISIONS.md`。

否则同类错误还会重复出现。

### 规则 5：planner 先生成执行介质

在复杂任务里，planner 不应只给一句话任务，而应优先准备：

- 计划文件
- 子任务表
- 设计/认知指南
- 初始脚手架
- 测试输出目录或记录位置

这样后续 agent 的上下文更稳定，返工率更低。

### 规则 6：重测聚焦失败项

如果上一轮测试已经列出问题，下一轮测试优先验证这些问题是否修复。

只有在页面或模块被大改时，才重新做全量测试。

---

## 调度优先级

当多个角色意见冲突时，建议采用下面的优先级：

```text
MANIFESTO / AGENTS
  > PRODUCT / REQUIREMENTS
  > WORKFLOW
  > ARCHITECTURE / DESIGN
  > IMPLEMENTATION
  > MEMORY
```

含义是：

- 如果实现和需求冲突，以需求为准
- 如果需求和总原则冲突，以总原则为准
- 如果流程和产品目标冲突，优先产品目标，再修流程

在测试维度冲突时，建议补一条默认优先级：

```text
结构与信息正确性
  > 可用性与稳定性
  > 视觉精致度
  > 动效表现
```

也就是先保证信息和结构对，再优化美观和动效。

---

## 闭环关系

APOS 不是线性流水线，而是一个闭环系统。

```text
需求提出
  -> 选择 workflow
  -> planner 产出计划 / 指南 / 脚手架
  -> 分配 agents
  -> 完成实现
  -> review / test
  -> 记录 decisions / lessons / patterns
  -> 更新 tasks / roadmap / requirements
```

这里最关键的是最后两步：

- 没有进入 `05-memory`，系统不会成长
- 没有回写 `02-product`，系统不会进化

所以 `memory` 不是资料库，而是调度回路的一部分。

---

## 推荐落地规则

为了让这套调度真正可执行，建议补 4 条操作规则：

### 规则 1

所有任务先落到 `02-product/TASKS.md`，再进入具体 workflow。

### 规则 2

所有跨角色任务都必须标记当前 owner。

建议状态格式：

```text
[状态] 任务标题
Owner: planner / designer / frontend / backend / reviewer / tester
Next: 下一个角色
Inputs: 输入文件
Outputs: 输出文件
Skills: 使用过的 skill；未使用则写 none
Writeback: 回写文件
```

### 规则 3

所有被 review 或 test 打回的任务，都要在 `05-memory/DECISIONS.md` 或 `LESSONS.md` 留痕。

这样才能逐步减少重复犯错。

### 规则 4

复杂任务默认要求执行角色只向主编排者返回：

- 当前结果状态
- 产物路径
- 是否需要下一轮处理

不要把大段实现说明直接塞回主对话。

---

## 自进化检查

APOS 每完成一轮任务后，都应做一次轻量自检：

- 产品目标是否发生变化，如果是，更新 `02-product/REQUIREMENTS.md` 或 `PRODUCT.md`
- 任务状态是否变化，如果是，更新 `02-product/TASKS.md`
- 是否出现新决策，如果是，更新 `05-memory/DECISIONS.md`
- 是否出现新踩坑，如果是，更新 `05-memory/LESSONS.md`
- 是否出现可复用方法，如果是，更新 `05-memory/PATTERNS.md`
- 系统能力是否变化，如果是，更新 `05-memory/EVOLUTION.md`

如果这些回写都没有发生，任务只能算完成了产出，不能算推动了 APOS 进化。

---

## 最终结论

APOS 的调度关系可以概括为：

> **Product 定义目标，Workflow 负责编排，Planner 先铺路，Agents 负责执行，Reviewer/Tester 负责收口，Memory 负责进化。**

如果你希望系统稳定、可扩展、适合 AI 协作，这套关系已经足够作为 APOS v1.0 的正式调度模型。





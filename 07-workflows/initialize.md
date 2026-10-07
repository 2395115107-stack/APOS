# Initialize Workflow

## 目标

`initialize.md` 定义把一个项目接入 APOS（或把 APOS 复制到新项目）的标准流程。

它适用于：

- 全新项目第一次使用 APOS
- 已有项目引入 APOS
- 项目长期停滞后的重新进入

不适用于：

- 日常新功能，使用 `new-feature.md`
- 系统自身的文档整理，使用 `memory-review.md`

它的产出不是代码，而是一份**项目地图**和一套**最小可验证基线**。

---

## 核心原则

1. 先盘点，再补齐，不凭印象初始化
2. 产品文档先于技术文档
3. 每个缺失文件先建最小可用版本，不追求一次写满
4. 初始化完成时，必须存在一条可运行的验证方式
5. 初始化结论必须回写 memory

---

## 输入文件

- `01-core/AGENTS.md`
- `APOS.md`（目录方案）
- 被初始化项目的现有文件（如果有）

---

## 流程总览

```text
进入项目
  -> Step 1: planner 盘点结构
  -> Step 2: 按层读取现有文档
  -> Step 3: 检测缺口
  -> Step 4: 补齐最小产品入口
  -> Step 5: 建立验证基线
  -> Step 6: 生成项目地图并回写
```

---

## Step 1: 盘点结构

Owner: `planner`

### 任务

列出项目当前的全部目录和关键文件，判断三种情况：

- 空项目：直接按 APOS 目录方案创建骨架
- 已有项目：标记哪些层已有事实源，哪些为空
- 停滞项目：标记哪些文档可能已过期

### 输出

```text
Owner: planner
Next: planner
Outputs: 结构盘点清单
Skills: none
Writeback: 无（盘点属于临时产物，进入报告）
```

---

## Step 2: 按层读取现有文档

Owner: `planner`

### 任务

按固定顺序读取已有内容：

```text
01-core -> 02-product -> 03-design -> 04-development -> 05-memory -> 06-references -> 07-workflows -> 08-agents
```

每层只回答一个问题：

| 层 | 问题 |
|---|---|
| 01-core | 这个项目遵循什么规则 |
| 02-product | 要做什么、做到什么算成功 |
| 03-design | 长什么样、遵循什么体验原则 |
| 04-development | 技术上怎么落地、怎么验证 |
| 05-memory | 已经学到了什么 |
| 06-references | 在向谁学习 |
| 07-workflows | 有哪些流程可用 |
| 08-agents | 有哪些角色可用 |

---

## Step 3: 检测缺口

Owner: `planner`

### 检查项

- 缺失文件：APOS.md 中列出但项目里不存在的
- 空壳文件：存在但没有实质内容的
- 断裂引用：文档里引用了不存在的路径
- 过期信息：与当前现实明显矛盾的描述

缺口分三级：

- `P0`：没有它就无法进入 `new-feature.md`（如 REQUIREMENTS、TASKS）
- `P1`：影响质量收口（如 DESIGN_SYSTEM、TECH_STACK）
- `P2`：可以以后补（如 references、模板）

---

## Step 4: 补齐最小产品入口

Owner: `planner`，必要时协同 `architect` / `designer`

### 任务

按 P0 → P1 顺序补齐文件，每个文件只写最小可用版本：

- `02-product/PRODUCT.md`：一段话产品定义
- `02-product/REQUIREMENTS.md`：当前需求、成功标准、本轮不做
- `02-product/TASKS.md`：状态说明 + 第一个任务
- `04-development/TECH_STACK.md`：技术选型与运行、测试命令
- `03-design/DESIGN_SYSTEM.md`：涉及 UI 时建立最小规范

已有项目引入 APOS 时，不重写事实，只建立入口并引用现有文档。

### 输出

```text
Owner: planner
Next: architect / designer / frontend / backend
Outputs: 补齐后的文档
Skills: none
Writeback: 02-product/TASKS.md
```

---

## Step 5: 建立验证基线

Owner: `architect` / `backend`

### 任务

确认项目存在至少一条 L1 级验证方式（见 `loop.md` 验证阶梯）：

- 能运行的构建或测试命令，或
- 明确的手工验证清单

把命令写入 `04-development/TECH_STACK.md`。没有验证基线，初始化不算完成。

---

## Step 6: 项目地图与回写

Owner: `planner`

### 任务

在 `02-product/PRODUCT.md` 末尾追加项目地图：

```text
## 项目地图

- 项目一句话：{定义}
- 当前阶段：{阶段}
- 验证方式：{命令或清单}
- 下一个任务：{TASKS.md 中的任务}
- 已知缺口：{P1 / P2 列表}
```

同时完成：

- `RUNS.md` 记录本次初始化
- `DECISIONS.md` 记录关键选型（如有）
- `EVOLUTION.md` 记录系统变化（如是首次接入 APOS）

### 收口输出

```text
初始化完成
Owner: planner
Next: new-feature / next task
Outputs: 项目地图, 补齐后的文档
Skills: {使用过的 skill；未使用则写 none}
Writeback: 02-product/*, 05-memory/RUNS.md, 05-memory/DECISIONS.md, 05-memory/EVOLUTION.md
```

---

## 质量门槛

初始化不能在以下情况标记完成：

- `02-product/` 没有可用的 REQUIREMENTS 和 TASKS
- 没有任何验证基线
- 缺口检测只说"有一些"，没有分级列表
- memory 没有回写

---

## 反模式

- 不盘点就开始创建一堆空模板
- 一次写满所有文档，半年后全部过期
- 把已有项目的事实源推翻重写
- 初始化完不留下任何可验证的东西

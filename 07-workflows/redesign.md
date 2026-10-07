# Redesign Workflow

## 目标

`redesign.md` 定义页面或体验重构的标准流程。

它适用于：

- 页面整体重构
- 信息层级或交互路径调整
- 视觉方向或品牌更新

不适用于：

- 新功能（走 `new-feature.md`）
- 局部样式微调（走 `new-feature.md` 的轻量路径）
- 纯技术重构（走 `new-feature.md` 的技术驱动链路）

---

## 核心原则

1. **先定义不变项**：重构前先写下什么不能变
2. **设计先行**：designer 产出结构判断，frontend 不自行决定层级
3. **有对比基线**：重构前留存旧状态，重构后逐项对比
4. **专项验收**：按维度启用 tester，而不是一个 tester 查所有
5. **设计系统回写**：重构产出的新模式必须沉淀回 `DESIGN_SYSTEM.md`

---

## 输入文件

- `02-product/REQUIREMENTS.md`
- `02-product/TASKS.md`
- `03-design/DESIGN_SYSTEM.md`
- 被重构页面的当前实现
- `05-memory/PATTERNS.md`（相关体验模式）

---

## 流程总览

```text
重构需求进入
  -> Step 1: planner 明确目标与不变项
  -> Step 2: designer 产出设计判断
  -> Step 3: 建立对比基线
  -> Step 4: frontend 实现
  -> Step 5: review + 专项测试
  -> Step 6: 回写与收口
```

---

## Step 1: 明确目标与不变项

Owner: `planner`

### 必须回答

- 为什么重构：现在的问题是什么
- 成功标准：重构后哪些体验指标变好
- 不变项：哪些功能、内容、路径不能丢
- 边界：本轮哪些页面和状态不做

### 输出

```text
Owner: planner
Next: designer
Outputs: 重构目标与不变项清单
Skills: none
Writeback: 02-product/REQUIREMENTS.md
```

不变项清单缺失，不进入实现。

---

## Step 2: 设计判断

Owner: `designer`

### 任务

产出结构级判断，落文件：

- 信息层级：先看什么、后看什么
- 交互路径：用户从哪进、经过什么、到哪去
- 视觉方向：与设计系统的关系（沿用 / 扩展 / 局部新增）
- 状态覆盖：空态、加载态、错误态、极端内容

### 输出

```text
Owner: designer
Next: frontend
Outputs: 设计指引（路径写入任务条目）
Skills: {可选视觉 / 设计类 skill，由任务上下文决定}
Writeback: 03-design/DESIGN_SYSTEM.md（如有新模式）
```

---

## Step 3: 建立对比基线

Owner: `frontend`

- 留存重构前页面的截图与关键行为描述
- 列出重构后需要逐项对比的检查点（来自不变项 + 成功标准）
- 基线与检查点写入任务条目，供专项 tester 使用

---

## Step 4: 实现

Owner: `frontend`

- 按设计指引实现，层级和路径不自创
- 复用设计系统既有组件与模式
- 交付时对照基线自查，并在返回中说明偏离点

---

## Step 5: Review 与专项测试

Owner: `reviewer` + 专项 tester

### reviewer

- 确认实现符合设计指引和不变项
- 检查行为回归（重构最容易破坏的是旧路径）

### 专项 tester

按维度并行启用（orchestrator-workers 模式）：

- `tester-layout`：结构与层级对比基线
- `tester-quality`：视觉与状态覆盖
- `tester-performance`：大页面或重交互时
- `tester-accessibility`：可访问性敏感页面

### 输出

```text
Owner: reviewer
Next: frontend / tester / planner
Outputs: findings, 各专项测试报告
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/LESSONS.md
```

---

## Step 6: 回写与收口

Owner: `planner`

- 确认的新模式写入 `03-design/DESIGN_SYSTEM.md`
- 失败与修正经验写入 `05-memory/LESSONS.md`
- `TASKS.md` 收口，`RUNS.md` / `EVALS.md` 记录本轮

### 收口输出

```text
Redesign 完成
Owner: planner
Next: none / next task
Outputs: 新页面, 设计指引, 测试报告
Skills: {本轮用过的主要 skill；未使用则写 none}
Writeback: 02-product/TASKS.md, 03-design/DESIGN_SYSTEM.md, 05-memory/*
```

---

## 质量门槛

重构不能在以下情况标记完成：

- 不变项没有逐项核对
- 没有对比基线
- 只做了"新样子好看"，没有验证旧路径
- 新模式没有回写设计系统

---

## 反模式

- designer 缺席，frontend 边写边定层级
- 重构顺带改需求
- 没有基线，全靠"感觉变好了"
- 一次重构波及所有页面

# New Feature Workflow

## 目标

`new-feature.md` 定义 APOS 中“新增功能”的标准流程。

它适用于：

- 新页面
- 新交互
- 新接口
- 新业务流程
- 新模块
- 现有功能的明显扩展

不适用于：

- 紧急线上修复，使用 `hotfix.md`
- 单纯视觉重构，使用 `redesign.md`
- 纯 review，使用 `review.md`

---

## 核心原则

1. 先确认目标，再拆任务
2. 先准备执行介质，再进入实现
3. 先 review，再 test
4. 测试失败回到原 owner 修复
5. 完成后必须回写 `05-memory/` 和 `02-product/`

---

## 输入文件

新功能开始前，至少需要这些输入：

- `01-core/AGENTS.md`
- `02-product/PRODUCT.md`
- `02-product/REQUIREMENTS.md`
- `02-product/TASKS.md`
- `03-design/DESIGN_SYSTEM.md`（如果涉及 UI/UX）
- `04-development/TECH_STACK.md`（如果涉及实现）
- `05-memory/DECISIONS.md`
- `05-memory/LESSONS.md`
- `05-memory/PATTERNS.md`

如果某些文件还不存在，planner 应创建最小可用版本或标记缺口。

---

## 流程总览

```text
需求进入
  -> Step 1: planner 澄清目标
  -> Step 2: planner 拆任务并准备执行介质
  -> Step 3: architect / designer 按需介入
  -> Step 4: frontend / backend 实现
  -> Step 5: reviewer 审查
  -> Step 6: tester 验收
  -> Step 7: 修正循环
  -> Step 8: 回写 memory 和 product
```

---

## Step 1: 目标澄清

Owner: `planner`

### 任务

确认新功能不是一句实现指令，而是一个真实产品目标。

必须回答：

- 目标用户是谁
- 用户要完成什么事
- 当前痛点是什么
- 成功标准是什么
- 这次功能不做什么

### 输出

```text
Owner: planner
Next: planner / architect / designer
Outputs: 目标澄清结果
Writeback: 02-product/REQUIREMENTS.md
```

### 进入下一步条件

- 目标清楚
- 成功标准清楚
- 边界清楚

如果不清楚，先补 `02-product/REQUIREMENTS.md`。

---

## Step 2: 任务拆分与执行介质

Owner: `planner`

### 任务

把功能拆成可执行、可验证的任务。

必须产出：

- 子任务列表
- owner / next owner
- 输入文件
- 输出文件
- 回写文件
- 是否需要专项 tester

复杂功能还应准备：

- 计划文件
- 页面 / 模块级设计或认知指引
- 初始脚手架建议
- 测试报告目录或报告命名规则

### 输出

```text
Owner: planner
Next: architect / designer / frontend / backend
Outputs: 任务拆分, 执行介质
Writeback: 02-product/TASKS.md
```

### 进入下一步条件

- 每个任务都可以独立交付或验证
- 每个任务都有 owner 和 next owner
- 每个任务都有明确输入和输出

---

## Step 3: 架构与设计判断

Owner: `architect` / `designer`

### 何时需要 architect

- 新增数据模型
- 新增 API 或服务
- 权限、状态、缓存、性能、部署受影响
- 多模块依赖复杂

### 何时需要 designer

- 新页面或新交互
- 用户路径发生变化
- 信息层级或视觉表达不清
- 需要设计系统约束

### 输出

```text
Owner: architect / designer
Next: frontend / backend
Outputs: 技术约束 / 设计指引
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/DECISIONS.md, 05-memory/PATTERNS.md
```

### 进入下一步条件

- 实现角色知道边界
- 风险点已标明
- 必要的设计和技术约束已落文件

---

## Step 4: 实现

Owner: `frontend` / `backend`

### 任务

按任务输入和约束实现功能。

实现角色必须：

- 读取需求、技术栈、设计系统、相关 memory
- 复用现有代码模式
- 按任务选择必要 skills
- 完成基础自测
- 输出产物路径，不把大段实现说明塞回主上下文

### 输出

```text
Owner: frontend / backend
Next: reviewer
Outputs: {代码文件路径}
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/LESSONS.md（如有经验）
```

### 进入下一步条件

- 实现已落文件
- 基础自测完成
- 已说明是否偏离原方案

---

## Step 5: Review

Owner: `reviewer`

### 任务

优先检查：

- 功能是否符合需求
- 是否有行为回归
- 是否有边界遗漏
- 是否有缺失测试
- 是否违反架构、设计、技术栈约束
- 是否需要专项 tester

### 输出

```text
Owner: reviewer
Next: tester / frontend / backend
Outputs: findings 或通过结论
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/LESSONS.md
```

### 进入下一步条件

- 无阻塞级问题
- 或问题已退回对应 owner 修复

---

## Step 6: Test

Owner: `tester` 或专项 tester

### 默认测试

通用 `tester` 验证：

- 核心路径
- 边界条件
- 异常路径
- 回归风险

### 专项测试

按需启用：

- `tester-layout`
- `tester-quality`
- `tester-performance`
- `tester-accessibility`

### 输出

```text
测试结果：PASS / FAIL
Owner: tester
Next: frontend / backend / reviewer
Outputs: 测试报告路径
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/LESSONS.md
```

### 进入下一步条件

- PASS：进入回写
- FAIL：进入修正循环

---

## Step 7: 修正循环

Owner: 原实现 owner

### 规则

- 测试失败优先回到原 owner
- 修正时读取完整测试报告
- 一次性处理本轮所有已知问题
- 重测只验证上一轮失败项
- 如果修改范围很大，再做全量 review / test

### 最大轮次

默认最多 3 轮。

如果 3 轮后仍失败，planner 必须重新判断：

- 是否需求不清
- 是否架构或设计方向错误
- 是否任务拆分过大
- 是否需要人工决策

### 输出

```text
Owner: frontend / backend / designer / architect
Next: tester / reviewer / planner
Outputs: 修正产物路径
Writeback: 05-memory/LESSONS.md
```

---

## Step 8: 回写与收口

Owner: `planner`，按需协同其它角色

### 必须回写

- `02-product/TASKS.md`：任务状态
- `05-memory/DECISIONS.md`：关键决策
- `05-memory/LESSONS.md`：踩坑和修复经验
- `05-memory/PATTERNS.md`：可复用模式

### 按需回写

- `02-product/REQUIREMENTS.md`：需求发生变化
- `02-product/ROADMAP.md`：影响阶段计划
- `03-design/DESIGN_SYSTEM.md`：设计系统发生变化
- `04-development/TECH_STACK.md`：技术栈或架构约定发生变化
- `08-agents/*.md`：角色职责或 skills 路由发生变化

### 收口输出

```text
新功能完成
Owner: planner
Next: none / release / next task
Outputs: 产物路径, 测试报告路径
Skills: {本轮用过的主要 skill；未使用则写 none}
Writeback: 02-product/TASKS.md, 05-memory/*
```

---

## 状态模板

`02-product/TASKS.md` 中建议使用：

```text
[状态] 任务标题
Owner: planner / architect / designer / frontend / backend / reviewer / tester
Next: 下一角色
Inputs: 输入文件
Outputs: 输出文件
Skills: 使用过的 skill；未使用则写 none
Writeback: 回写文件
```

状态值：

- `TODO`
- `IN_PROGRESS`
- `REVIEW`
- `TEST`
- `FIXING`
- `DONE`
- `BLOCKED`

---

## 质量门槛

新功能不能在以下情况标记完成：

- 需求没有明确成功标准
- 没有 owner / next owner
- 实现没有落文件
- review 未完成
- test 未完成
- 失败经验没有回写
- 文档与实现明显不一致但未说明原因

---

## 最终原则

新功能不是“写完代码”就结束。

它结束于：

```text
产品状态更新
  + 实现完成
  + review/test 通过
  + 经验回写
  + 文档一致
```

# Review Workflow

## 目标

`review.md` 定义 APOS 中代码和产物评审的标准流程。

它适用于：

- 一轮实现完成后的正式评审
- 任务收口前的质量判断
- `hotfix.md` 之后的补充全量评审
- 发布前检查（配合 `release.md`）

不适用于：

- 测试执行，使用 tester（本流程负责调度）
- 系统自身文档复盘，使用 `memory-review.md`

---

## 核心原则

1. **确定性检查优先**：先跑机器能判的，再进入判断性评审
2. **评审者不修复**：reviewer 只输出 findings，修复退回原 owner
3. **生产者不自审**：关键产出不能由产出它的同一个上下文自评通过
4. **复评只验证失败项**：不重复全量审查
5. **失败必须回写 memory**

---

## 输入文件

- `02-product/REQUIREMENTS.md`
- `02-product/TASKS.md` 中当前任务条目
- 被评审的产物（代码 / 文档 / 报告）
- `04-development/TECH_STACK.md`
- `04-development/AGENT_INTERFACE.md`（输出格式约定）
- `05-memory/LESSONS.md` 中相关条目

---

## 流程总览

```text
进入评审
  -> Step 1: 明确评审范围
  -> Step 2: 确定性检查
  -> Step 3: 判断性评审
  -> Step 4: 输出 findings
  -> Step 5: 修复与复评
  -> Step 6: 回写收口
```

---

## Step 1: 明确评审范围

Owner: `reviewer`

### 任务

从 `TASKS.md` 确认：

- 本次要评审的产物路径
- 对应的需求和成功标准
- 声明不做的事（避免越范围评审）

范围不清时，先退回 planner 补任务条目，不凭猜测评审。

---

## Step 2: 确定性检查

Owner: `reviewer`（或直接运行既有检查）

2026 年 evaluation 实践的共识是：确定性检查能以极低成本拦住大部分问题，必须放在判断性评审之前。

按验证阶梯从高到低优先执行 L1 / L2：

- L1：构建、测试、schema、命令退出码
- L2：lint、格式、文档字段完整性（`Owner / Next / Inputs / Outputs / Skills / Writeback` 是否齐全）

任何 L1 / L2 失败直接生成 findings，不进入 Step 3。

---

## Step 3: 判断性评审

Owner: `reviewer`

### 评审维度（按优先级）

1. 需求符合性：是否做了需求要求的事
2. 行为正确性：bug、回归、边界、异常路径
3. 数据与安全：数据流、权限、错误处理
4. 架构与设计约束：是否偏离 `DECISIONS.md` 和设计系统
5. 测试缺口：哪些行为没有验证
6. 风格与一致性：最后才看

机器能查的（风格、语法、格式）不占用判断性评审，这是 2026 年 code review 实践的分工共识：让机械检查兜住低级问题，评审聚焦架构、行为和风险。

---

## Step 4: 输出 findings

Owner: `reviewer`

按 `04-development/AGENT_INTERFACE.md` 的报告格式落盘到 `10-reports/{RUN-ID}/review.md`。

每条 finding 必须包含：

- 严重度：`BLOCKER` / `MAJOR` / `MINOR` / `NIT`
- 位置：文件路径或行为描述
- 影响：一句话
- 建议：一句话

### 输出

```text
Owner: reviewer
Next: frontend / backend / designer / tester
Outputs: 10-reports/{RUN-ID}/review.md
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/LESSONS.md
```

---

## Step 5: 修复与复评

Owner: 原 owner 修复，`reviewer` 复评

这是一个 evaluator-optimizer 环：评审者按固定标准评，实现者按 findings 改，循环到通过或到达上限。

### 规则

- BLOCKER / MAJOR 必须修复；MINOR 应修复；NIT 可攒到下一轮
- 修复方读取完整报告，一次性处理本轮全部问题
- 复评只验证上一轮失败项（PAT-004）
- 修改范围超过原任务边界时，重新走全量 Step 2-3
- 默认最多 3 轮；3 轮后仍失败，退回 planner 重新判断（见 `new-feature.md` Step 7）

---

## Step 6: 回写收口

Owner: `reviewer` / `planner`

- 评审结论写入 `10-reports/{RUN-ID}/`
- 重复出现的问题写入 `05-memory/LESSONS.md`
- 评审发现的文档与实现偏离，提醒对应 owner 同步文档
- `TASKS.md` 更新任务状态

---

## 并行评审

对大范围改动，可按 orchestrator-workers 模式拆分：

```text
reviewer（编排）
  -> reviewer-arch：架构与数据流
  -> reviewer-sec：安全与权限
  -> tester-layout / tester-quality（按需）
  -> 汇总为一份 findings
```

拆分时每个子评审只读自己维度的上下文，汇总由主 reviewer 负责。

---

## 质量门槛

评审不能在以下情况写通过：

- 没有跑过 L1 / L2 检查
- findings 没有严重度和位置
- BLOCKER 未修复就放行
- 实现者自评"我检查过了"替代复评
- 报告没有落盘

---

## 反模式

- 评审变成润色：先提风格建议，后提行为风险
- reviewer 顺手改代码
- 用一句"整体没问题"代替结构化 findings
- 复评把所有东西再查一遍
- 只看 diff 不看需求

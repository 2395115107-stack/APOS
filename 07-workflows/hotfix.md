# Hotfix Workflow

## 目标

`hotfix.md` 定义紧急修复的标准流程：在生产故障、阻塞缺陷或安全问题发生时，以最小代价止血，并在事后补全质量闭环。

它适用于：

- 线上功能不可用或大面积报错
- 数据错误或有丢失风险
- 安全漏洞需要立即处置
- 发布流程被缺陷阻塞

不适用于：

- 一般 bug（走 `new-feature.md` 或 `review.md`）
- 可以排期的技术债

---

## 核心原则

1. **先止血，再治本**：第一步是恢复可用，不是找到完美修复
2. **回滚优先于硬修**：能回滚就不现场写新代码
3. **时间盒**：每个阶段有明确时限，超时即升级人工
4. **最小 diff**：hotfix 只做让问题消失的最小改动
5. **记录不省略**：快不等于乱，事后必须补全 review 和 memory

---

## 输入文件

- `02-product/TASKS.md`
- `04-development/TECH_STACK.md`（运行、部署、回滚方式）
- `04-development/PERMISSIONS.md`（哪些操作需要人工确认）
- 故障现象描述（用户报告、日志、监控）

---

## 流程总览

```text
故障进入
  -> Step 1: 确认问题边界（限 15 分钟）
  -> Step 2: 选择止血方式
  -> Step 3: 最小实现
  -> Step 4: 快速验证
  -> Step 5: 恢复与观察
  -> Step 6: 事后补全（24 小时内）
```

---

## Step 1: 确认问题边界

Owner: `planner`

限时 15 分钟回答：

- 影响面：哪些用户、哪些功能、有没有数据风险
- 复现方式：稳定复现还是偶发
- 最近变更：最后一次部署或改动是什么
- 止血候选：回滚 / 开关降级 / 修复

超过 15 分钟没有结论，直接进入人工决策，不要继续调查。

### 输出

```text
Owner: planner
Next: backend / frontend
Outputs: 问题边界记录（进入报告）
Skills: none
Writeback: 10-reports/{RUN-ID}/incident.md
```

---

## Step 2: 选择止血方式

Owner: `planner` + `architect`

按优先级选择：

1. 回滚到上一个正常版本（首选，零新代码）
2. 开关 / 配置降级（关闭出问题的功能）
3. 最小修复（只在没有回滚和降级选项时）

涉及 `PERMISSIONS.md` 高风险操作（部署、删数据、改配置）时，先取得人工确认。

---

## Step 3: 最小实现

Owner: `backend` / `frontend`

- 只改与故障直接相关的代码
- 不顺手重构、不顺手修别的 bug
- 每处修改在报告中说明为什么它能让问题消失

### 输出

```text
Owner: backend / frontend
Next: reviewer
Outputs: 修复 diff
Skills: {使用过的 skill；未使用则写 none}
Writeback: 10-reports/{RUN-ID}/incident.md
```

---

## Step 4: 快速验证

Owner: `reviewer` / `tester`

hotfix 的验证允许降级，不允许缺席：

- 至少一项 L1 检查：构建通过 + 针对故障的定向测试
- reviewer 快速过一遍 diff，只看回归风险
- 完整评审延后到 Step 6

验证失败且无法快速修正时，回到 Step 2 优先回滚。

---

## Step 5: 恢复与观察

Owner: `backend` + `planner`

- 部署或恢复服务（人工确认后执行）
- 按故障严重度观察一个明确的时间窗（例如 30 分钟无新增报错）
- 观察期内不叠加新的变更

---

## Step 6: 事后补全

Owner: `reviewer` + `planner`，24 小时内完成

止血不等于修复完成。事后必须补全：

1. **全量 review**：对 hotfix diff 走 `review.md` 完整流程
2. **根因归类**：在 `EVALS.md` 中归类失败来源（`IMPL` / `ARCH` / `TEST` / `REQ` ...）
3. **完整修复**：如果止血是临时方案，建立正式任务根治
4. **回写 memory**：
   - `DECISIONS.md`：止血选型和根因结论
   - `LESSONS.md`：如何更早发现这类问题
   - `RUNS.md` / `EVALS.md`：本次事件记录
   - `TECH_STACK.md`：回滚 / 监控手段如需更新

### 收口输出

```text
Hotfix 完成
Owner: planner
Next: review / new-feature / none
Outputs: incident 报告, 修复 diff, 补全评审报告
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/RUNS.md, 05-memory/EVALS.md, 05-memory/DECISIONS.md, 05-memory/LESSONS.md
```

---

## 终态

hotfix 只允许以下终态（沿用 `loop.md` 命名）：

- `SUCCESS`：服务恢复 + 观察通过 + 事后补全已排期
- `BLOCKED`：无法止血，需人工决策
- `EXHAUSTED`：时间盒用尽，升级人工

禁止把"代码改完了"写成 hotfix 成功。

---

## 反模式

- 没有回滚预案就现场大改
- hotfix 顺手夹带重构
- 以"紧急"为由跳过全部验证和记录
- 止血后不写根因，同类故障反复发生
- 在观察期继续叠加变更

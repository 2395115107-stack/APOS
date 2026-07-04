# Evals

## 目标

`EVALS.md` 记录 APOS 的评估标准和评估结果。

它不是单次测试报告，而是长期观察 APOS 是否变得更可靠的地方。

## 评估维度

### 1. Product Fit

任务是否真的服务产品目标。

通过标准：

- 需求目标明确
- 成功标准明确
- 不把实现方案误当成真实需求

### 2. Workflow Fit

任务是否进入了正确 workflow。

通过标准：

- workflow 明确
- owner / next owner 明确
- 输入输出和回写文件明确

### 3. Agent Fit

角色是否按边界工作。

通过标准：

- planner 不替代实现
- reviewer 不替代 planner
- tester 只读
- frontend / backend 不改写产品目标

### 4. Memory Fit

经验和决策是否回写。

通过标准：

- decision 进入 `DECISIONS.md`
- lesson 进入 `LESSONS.md`
- pattern 进入 `PATTERNS.md`
- 系统变化进入 `EVOLUTION.md`

### 5. Verification Fit

是否经过 review / test / self-check。

通过标准：

- 有明确验证方式
- 失败原因可追踪
- 修正轮次可记录

## 失败分类

失败时，必须归类到至少一个来源：

- `REQ`：需求不清
- `PLAN`：任务拆分错误
- `ARCH`：架构判断错误
- `DESIGN`：设计判断错误
- `IMPL`：实现错误
- `REVIEW`：评审漏掉问题
- `TEST`：测试漏掉问题
- `MEMORY`：没有回写经验或决策
- `DOCS`：文档与实现不一致
- `TOOLS`：工具、skill 或环境问题

## Eval 模板

```text
## EVAL-{YYYYMMDD}-{序号}: {任务标题}

Run: RUN-{YYYYMMDD}-{序号}
Status: PASS / FAIL / PARTIAL
Failure Class: REQ / PLAN / ARCH / DESIGN / IMPL / REVIEW / TEST / MEMORY / DOCS / TOOLS / none
Product Fit: PASS / FAIL
Workflow Fit: PASS / FAIL
Agent Fit: PASS / FAIL
Memory Fit: PASS / FAIL
Verification Fit: PASS / FAIL

### 结论

{一句话判断}

### 改进项

- {如无，写 none}
```

---

## EVAL-20260704-001: APOS 最小可运行系统补齐

Run: RUN-20260704-001
Status: PASS
Failure Class: none
Product Fit: PASS
Workflow Fit: PASS
Agent Fit: PASS
Memory Fit: PASS
Verification Fit: PARTIAL

### 结论

APOS 已具备最小可运行闭环，但验证仍主要是文档和文件完整性检查，还没有自动化机械检查。

### 改进项

- 补 `04-development/AGENT_INTERFACE.md`
- 补机械化文档检查
- 补正式 `review.md` / `hotfix.md` / `initialize.md`

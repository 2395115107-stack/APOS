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

---

## EVAL-20261007-001: v1.1 收口——补齐常用 workflow 与 agent 接口

Run: RUN-20261007-001
Status: PASS
Failure Class: none
Product Fit: PASS
Workflow Fit: PASS
Agent Fit: PASS
Memory Fit: PASS
Verification Fit: PARTIAL

### 结论

缺口分析 P0 / P1 的文档层缺口全部补齐，v1.1 完成。新文献（context engineering、spec-driven、deterministic-first evaluation）均已映射到具体接口文件，而非只停留在综述。

### 改进项

- Verification Fit 仍为 PARTIAL：机械检查脚本缺失，本次一致性核对为人工完成
- 九个 workflow 中只有 new-feature / loop / evaluation / memory-review 被实际使用过，initialize / review / hotfix / release / redesign 待实战验证
- 下一步建立评估集与回归样例库，避免评估只靠单次核对

---

## EVAL-20261007-002: v1.1 迭代三轮自检

Run: RUN-20261007-002
Status: PASS
Failure Class: none
Product Fit: PASS
Workflow Fit: PASS
Agent Fit: PASS
Memory Fit: PASS
Verification Fit: PASS

### 结论

Verification Fit 首次达到 PASS：机械检查落地后，文档一致性、引用可解析性、任务字段完整性都有了可重复的验证方式。本轮从检查到修复（20 处 → PASS）本身就是 check_docs.py 的第一次实战验证，并顺手闭环了最后一个待补 workflow。

### 改进项

- initialize / review / hotfix / release / redesign 仍待真实项目实战
- KNOWN_PENDING allowlist 需要在每次 memory-review 时复核
- 评估集与回归样例库仍未建立

# Frontier Agent Systems Gap Analysis

Date: 2026-07-04
Scope: APOS v1.0

## Sources

- OpenAI, Harness Engineering: https://openai.com/index/harness-engineering/
- Anthropic, Building Effective Agents: https://www.anthropic.com/engineering/building-effective-agents
- SWE-agent paper: https://arxiv.org/abs/2405.15793
- SWE-rebench paper: https://arxiv.org/abs/2505.20411
- Saving SWE-Bench paper: https://arxiv.org/abs/2510.08996

## 总判断

APOS 当前已经具备：

- 稳定目录
- 总规则
- 产品入口
- agent 角色
- new-feature workflow
- memory 回写
- 自进化入口

但从前沿 agent engineering 的角度看，还缺 7 个能力层。

---

## Gap 1: Workflow pattern taxonomy 不完整

### 来源启发

Anthropic 将 agentic systems 区分为 workflow 和 agent，并列出 prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer 等模式。

### APOS 现状

APOS 已经有 `new-feature.md`，但还没有明确区分：

- routing
- parallel tester
- evaluator-optimizer
- orchestrator-workers
- fixed workflow vs open-ended agent

### 建议补充

新增：

- `07-workflows/routing.md`
- `07-workflows/evaluator-optimizer.md`
- `07-workflows/parallel-review.md`

或先在 `07-workflows/README.md` 中加入 workflow pattern taxonomy。

---

## Gap 2: Agent-Computer Interface 还不够明确

### 来源启发

SWE-agent 论文强调，agent 使用计算机的接口设计会显著影响软件工程表现。

### APOS 现状

APOS 规定了 `Owner / Next / Inputs / Outputs / Skills / Writeback`，但还没有规定：

- 文件编辑约定
- 测试命令约定
- 日志读取约定
- 报告路径约定
- tool / skill 输入输出格式

### 建议补充

新增：

- `04-development/AGENT_INTERFACE.md`

内容包括：

- 如何读文件
- 如何报告修改
- 如何运行测试
- 如何写测试报告
- 如何处理失败
- 如何避免相对路径、隐式状态和大段上下文污染

---

## Gap 3: Evaluation loop 不够系统

### 来源启发

SWE-rebench 和 Saving SWE-Bench 都强调：静态、过期、污染的 benchmark 会误判 agent 能力，真实评估需要持续、新鲜、接近真实交互的任务。

### APOS 现状

APOS 有 tester 和 memory review，但还没有：

- 任务评估集
- 成功率记录
- 失败分类
- 回归样例库
- 每轮 agent 表现复盘

### 建议补充

新增：

- `05-memory/EVALS.md`
- `07-workflows/evaluation.md`

记录：

- 每次任务是否通过
- 失败来自需求、设计、架构、实现、测试还是文档
- 哪个 agent 反复出现问题
- 哪些 workflow 需要调整

---

## Gap 4: Observability / agent-readable logs 缺失

### 来源启发

Harness engineering 强调 agent 需要能看到环境反馈；Anthropic 也强调 agent 要从工具结果、代码执行等 ground truth 判断进展。

### APOS 现状

APOS 有 memory，但还没有专门的运行日志。

### 建议补充

新增：

- `05-memory/RUNS.md`

用于记录：

- 本次任务 ID
- 使用 workflow
- 参与 agents
- 使用 skills
- review / test 结果
- 修正轮次
- 最终状态

---

## Gap 5: Stopping conditions 和 human checkpoints 不够明确

### 来源启发

Anthropic 建议 agent 长任务应有检查点、阻塞时请求人类判断，并设置停止条件来控制成本和错误累积。

### APOS 现状

`new-feature.md` 有 3 轮修正上限，但其它流程还没有统一停止规则。

### 建议补充

在 `01-core/AGENTS.md` 或 `07-workflows/README.md` 增加：

- 最大修正轮次
- 什么时候必须停下来问人
- 什么情况标记 `BLOCKED`
- 什么情况允许低质量通过
- 什么情况必须回到 planner 重新拆任务

---

## Gap 6: Mechanical checks 缺失

### 来源启发

Harness engineering 强调关键约束应尽量机械化，而不是只靠文档提醒。

### APOS 现状

目前都是 Markdown 规则，还没有自动检查。

### 建议补充

后续增加：

- 文档完整性检查脚本
- 必需文件存在性检查
- `Owner / Next / Inputs / Outputs / Skills / Writeback` 字段检查
- memory 回写检查
- workflow 引用文件存在性检查

可新增目录：

- `09-tools/`

---

## Gap 7: Security / permissions model 还未成型

### 来源启发

前沿 agent 系统越来越强调 sandbox、权限、工具边界和监控。

### APOS 现状

APOS 已规定 tester 只读，但还没有统一权限模型。

### 建议补充

新增：

- `04-development/PERMISSIONS.md`

定义：

- 哪些 agent 可写文件
- 哪些 agent 只读
- 哪些操作需要用户确认
- 哪些操作禁止自动执行
- 网络、部署、删除、迁移等高风险操作如何处理

---

## 推荐优先级

### P0: 马上补

1. `04-development/AGENT_INTERFACE.md`
2. `05-memory/RUNS.md`
3. `05-memory/EVALS.md`
4. `07-workflows/memory-review.md` 已补，后续需要实际运行

### P1: 下一轮补

1. `07-workflows/review.md`
2. `07-workflows/hotfix.md`
3. `07-workflows/initialize.md`
4. `04-development/PERMISSIONS.md`

### P2: 系统增强

1. `09-tools/` 文档检查脚本
2. `07-workflows/evaluation.md`
3. `07-workflows/parallel-review.md`
4. workflow pattern taxonomy

## 结论

APOS 当前缺的不是更多 agent，而是：

```text
agent interface
  + evaluation loop
  + run logs
  + permissions
  + mechanical checks
```

这些会让 APOS 从“文档驱动系统”进一步进化为“可验证、可观测、可治理的 agent harness”。

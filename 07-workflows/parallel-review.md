# Parallel Review Workflow

## 目标

`parallel-review.md` 定义大范围改动或多维验收任务的并行评审编排。

它是 `review.md` 和专项 tester 的 orchestrator-workers 用法：主评审员拆维度、派发子评审、汇总 findings，不自己改代码。

## 什么时候使用

满足任一条件即可考虑：

- 改动横跨多个模块或多个页面
- 需要布局、视觉、性能、可访问性多个维度同时验收
- 全量评审单轮做不完，但各维度之间相对独立

如果改动只有一个维度，直接走 `review.md`，不要为并行而并行。

## 编排结构

```text
reviewer（编排者）
  -> 拆分评审维度，明确每路的输入文件与报告路径
  -> 子评审并行执行
  -> 汇总为一份 findings，统一严重度
  -> 退回对应 owner 修复
```

## 标准拆分

| 子评审 | 关注点 | 产出 |
|---|---|---|
| reviewer-arch | 架构、数据流、模块边界 | findings |
| reviewer-sec | 安全、权限、错误处理 | findings |
| tester-layout | 结构与信息层级对比基线 | 测试报告 |
| tester-quality | 视觉质量与状态覆盖 | 测试报告 |
| tester-performance | 性能敏感改动 | 测试报告 |
| tester-accessibility | 可访问性敏感改动 | 测试报告 |

按需启用 2-3 路，不要求每次全开。

## 编排规则

1. **拆分先落文件**：主编排者把每路的范围、输入、报告路径写入任务条目，再派发
2. **子评审只读自己的维度**：每个子评审只读完成本维度所需的上下文，不互相传染
3. **汇总统一口径**：严重度以 `AGENT_INTERFACE.md` 的 BLOCKER / MAJOR / MINOR / NIT 为准，由主编排者归一
4. **冲突上报**：两个子评审结论冲突时，主编排者不裁决技术问题，标记冲突并升级 planner / architect
5. **报告分别落盘**：各路报告写入 `10-reports/{RUN-ID}/`，汇总报告在头部列出全部子报告路径

## 输出格式

```text
Parallel Review 完成
Owner: reviewer
Next: frontend / backend / designer / planner
Outputs: 汇总报告路径, 各子报告路径
Skills: {使用过的 skill；未使用则写 none}
Writeback: 05-memory/LESSONS.md, 02-product/TASKS.md
```

## 质量门槛

- 每路子评审都有独立报告，不允许只交一份"综合感觉"
- 汇总报告必须列出：参与子评审、各自结论、冲突项（如有）
- BLOCKER 汇总遗漏视为编排失败

## 反模式

- 为了并行把一个任务拆给所有角色，没人负责汇总
- 子评审之间互相读取对方结论后再下判断（失去独立性）
- 并行轮次超过 5 路仍未收敛，却不退回 planner 重新拆任务

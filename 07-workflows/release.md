# Release Workflow

## 目标

`release.md` 定义发布前的检查流程，确保进入发布的内容满足 APOS 的完整闭环要求。

它适用于：

- 版本发布
- 对外交付
- 长周期任务收尾后的归档检查

不适用于：

- hotfix 上线（先走 `hotfix.md`，事后补本流程）
- 日常提交

---

## 核心原则

1. **检查清单化**：发布靠清单，不靠印象
2. **文档与实现一致**：说出去的内容必须和实际行为一致
3. **验证有证据**：每个通过项都有对应报告或命令输出
4. **有回滚预案才发布**
5. **发布也是任务**：要走 review / test / memory 回写

---

## 输入文件

- `02-product/PRODUCT.md`、`ROADMAP.md`、`REQUIREMENTS.md`、`TASKS.md`
- `05-memory/RUNS.md`、`EVALS.md`
- `04-development/TECH_STACK.md`
- 本轮所有 review / test 报告（`10-reports/`）

---

## 流程总览

```text
发布请求
  -> Step 1: 任务闭环检查
  -> Step 2: 文档一致性检查
  -> Step 3: 验证阶梯复核
  -> Step 4: 发布产物与回滚预案
  -> Step 5: 执行发布（人工确认）
  -> Step 6: 发布后观察与回写
```

---

## Step 1: 任务闭环检查

Owner: `reviewer`

检查：

- 本版本包含的任务在 `TASKS.md` 中全部为 `DONE`
- 没有任务带着 `BLOCKED` / 未修复 `BLOCKER` 进入发布
- `RUNS.md` 中本轮任务都有记录，`EVALS.md` 中都有评估
- 所有 `FAIL` 或 `PARTIAL` 评估都有明确处理说明

---

## Step 2: 文档一致性检查

Owner: `reviewer`

对照检查：

- `README.md` 描述的功能与实际一致
- `PRODUCT.md` / `ROADMAP.md` 与实际进度一致
- `TECH_STACK.md` 中的运行、测试命令可执行
- `DESIGN_SYSTEM.md` 与当前界面一致（如涉及）
- 已知问题已写入 `PRODUCT.md` 或发布说明，而不是留在对话里

发现不一致：小问题当场修，大问题退回对应 owner。

---

## Step 3: 验证阶梯复核

Owner: `tester` + `reviewer`

按 `loop.md` 的验证阶梯确认证据链：

- L1 / L2：最新一次构建、测试、lint 全部通过，且有记录
- L3：真实运行或部署预演的结果（如适用）
- L4：rubric / model judge 的结论（如使用，注明生产者不自审）
- L5：需要人工确认的点已列出

任何一层证据缺失，必须在发布说明中声明降级理由，或推迟发布。

---

## Step 4: 发布产物与回滚预案

Owner: `backend` / `frontend`

准备并写入报告：

- 发布产物：版本号、tag、产物路径
- 变更清单：本版本包含的主要变更和影响面
- 回滚预案：如何回退到上一版本、由谁执行、预计耗时
- 已知问题清单

没有回滚预案不允许进入 Step 5。

---

## Step 5: 执行发布

Owner: `planner` + 人工

发布属于 `PERMISSIONS.md` 高风险操作：

- agent 准备发布说明和命令，人工确认后执行
- 发布动作和确认人记录进报告
- 发布失败立即走 `hotfix.md`

---

## Step 6: 发布后观察与回写

Owner: `planner`

- 设定观察窗口，确认核心路径正常
- 回写：
  - `02-product/ROADMAP.md`：阶段状态更新
  - `02-product/TASKS.md`：发布任务收口
  - `05-memory/RUNS.md` / `EVALS.md`：发布记录
  - `05-memory/LESSONS.md`：发布过程中的踩坑

### 收口输出

```text
Release 完成
Owner: planner
Next: none / next version
Outputs: 发布说明, 报告路径
Skills: {使用过的 skill；未使用则写 none}
Writeback: 02-product/*, 05-memory/*
```

---

## 发布检查清单

发布前逐项确认：

```text
[ ] 本版本任务全部 DONE，无未处理 BLOCKER
[ ] RUNS / EVALS 记录完整
[ ] 构建与测试通过且有记录
[ ] README / PRODUCT / ROADMAP / TECH_STACK 与实现一致
[ ] 已知问题已写入发布说明
[ ] 版本号与 tag 就绪
[ ] 回滚预案就绪
[ ] 人工确认发布动作
```

---

## 质量门槛

发布不能在以下情况执行：

- 检查清单有未通过项却没有书面豁免
- 文档与实现明显不一致
- 没有回滚预案
- 验证证据缺失且未声明降级

---

## 反模式

- 发布前一晚才第一次跑全量检查
- 用"应该没问题"代替证据
- 发布后不观察、不回写
- 把已知问题瞒在发布说明之外

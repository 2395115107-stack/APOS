# APOS 小白使用指南

这份指南给第一次使用 APOS 的人。

你不需要先理解所有目录，也不需要先读完所有文档。你只要记住一句话：

> 先把需求说清楚，然后让 APOS 按流程推进。

---

## 30 秒开始

把下面这段话复制给 AI：

```text
使用 APOS，按 new-feature workflow 帮我推进这个需求：

我想做：{你想做什么}
用户是：{谁会用}
为什么做：{解决什么问题}
成功标准：{做到什么算完成}
本轮不做：{哪些先不做}
```

例子：

```text
使用 APOS，按 new-feature workflow 帮我推进这个需求：

我想做：一个课程详情页
用户是：想购买课程的学生
为什么做：让用户快速理解课程价值并下单
成功标准：用户能看到课程介绍、目录、价格和购买按钮
本轮不做：支付系统和用户登录
```

AI 接下来应该帮你做这些事：

1. 写入 `02-product/REQUIREMENTS.md`
2. 在 `02-product/TASKS.md` 建任务
3. 按 `07-workflows/new-feature.md` 拆步骤
4. 调用合适的 agent
5. 完成后写回 `05-memory/`

---

## 你最常用的 3 句话

### 1. 做新功能

```text
使用 APOS，按 new-feature workflow 推进这个需求：
{把你的需求写在这里}
```

### 2. 检查当前项目做得怎么样

```text
使用 APOS，按 evaluation workflow 评估最近一次任务，并更新 RUNS 和 EVALS。
```

### 3. 整理经验，让系统变聪明

```text
使用 APOS，按 memory-review workflow 整理 memory，清理过期经验，升级稳定 pattern。
```

---

## 你需要知道的 5 个文件

刚开始只看这 5 个就够：

1. `02-product/REQUIREMENTS.md`

写当前需求。

2. `02-product/TASKS.md`

看现在要做什么、做到哪一步。

3. `07-workflows/new-feature.md`

新功能怎么推进。

4. `05-memory/RUNS.md`

这次任务发生了什么。

5. `05-memory/EVALS.md`

这次任务做得怎么样。

其它文件以后再慢慢看。

---

## 不知道该填什么时

你可以只说一个很粗的想法：

```text
使用 APOS，先帮我把这个想法整理成需求：
{你的粗略想法}
```

AI 应该先问清：

- 用户是谁
- 场景是什么
- 成功标准是什么
- 这一版不做什么

然后再进入实现。

---

## APOS 怎么自己变聪明

每次任务结束后，APOS 会把结果写进 memory：

- `DECISIONS.md`：为什么这么决定
- `LESSONS.md`：踩了什么坑
- `PATTERNS.md`：哪些做法可以复用
- `EVOLUTION.md`：APOS 自己哪里变强了
- `RUNS.md`：这次任务怎么跑的
- `EVALS.md`：这次任务质量怎么样

简单说：

```text
做一次任务
  -> 记录过程
  -> 评估质量
  -> 总结经验
  -> 下次少犯错
```

---

## 最小规则

你只要记住：

- 不清楚需求时，先别急着做
- 每个任务都要有 owner
- 做完要 review / test
- 失败要写进 memory
- APOS 的目标是越用越聪明

---

## 第一次推荐操作

直接对 AI 说：

```text
使用 APOS，先帮我把下面这个想法整理成 REQUIREMENTS 和 TASKS：

{你的想法}
```

这就是开始。

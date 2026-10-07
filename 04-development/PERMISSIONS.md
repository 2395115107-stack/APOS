# Permissions

## 目标

`PERMISSIONS.md` 定义 APOS 的权限模型：哪些 agent 可以写什么、哪些操作必须人工确认、哪些操作禁止自动执行。

它来源于前沿 agent 系统的共同判断：

- Anthropic Building Effective Agents：长任务应设置检查点，阻塞时请求人类判断
- Harness engineering：权限和边界要尽量机械化，不能只靠提醒
- tester 只读是 APOS 的既有原则，本文件把它扩展为统一权限模型

---

## 权限原则

1. **默认最小权限**：agent 只拥有完成当前任务所需的读写范围
2. **验证角色只读**：tester 默认只读，reviewer 只在报告和 memory 层面写
3. **高风险操作人工确认**：不可逆、外发、发布类操作必须有人工确认记录
4. **越权即回写**：任何越权行为都要记录到 `05-memory/LESSONS.md`，并触发对应 agent 文档修订

---

## 权限矩阵

| 角色 | 读 | 写 | 说明 |
|---|---|---|---|
| planner | 全部文档 | `02-product/*`、`05-memory/*` | 不写实现产物 |
| architect | 全部文档 | `04-development/*`、`05-memory/*` | 技术约束与决策 |
| designer | 全部文档 | `03-design/*`、`05-memory/*` | 设计指引与规范 |
| frontend | 任务相关文件 | 代码与前端产物、`05-memory/LESSONS.md` | 不改产品目标 |
| backend | 任务相关文件 | 代码与服务产物、`05-memory/LESSONS.md` | 不改 UI 规范 |
| reviewer | 全部文档 | 报告（`10-reports/`）、`05-memory/LESSONS.md` | 不直接修业务代码 |
| tester | 任务相关文件 + 只读产物 | 报告（`10-reports/`）、`05-memory/LESSONS.md` | 不修改任何被测产物 |

所有角色的报告统一写入 `10-reports/{RUN-ID}/`，路径约定见 `04-development/AGENT_INTERFACE.md`。

---

## 高风险操作清单

以下操作默认禁止自动执行，必须先获得人工确认：

### 破坏性操作

- 删除文件、目录、分支、数据
- 覆盖 git 历史（rebase / force push）
- 数据库删除、迁移、批量改写

### 发布类操作

- 部署上线、发布 release、打版本 tag
- 修改 CI / 构建配置
- 修改权限或访问控制

### 外发类操作

- 向外部服务发送数据或请求付费 API
- 发送消息、邮件、通知
- 公开原本私有的内容

人工确认的方式：agent 说明操作内容、影响范围和回退方式，等待明确同意后再执行，并把确认记录写入当次报告。

---

## 人工检查点

除高风险操作外，以下情况必须停下来请求人工判断：

- 连续 3 轮修正仍然失败
- 需要在两个产品方向之间做选择
- 发现需求、文档、实现三方互相矛盾
- 任务需要的输入文件或权限缺失
- 修复需要绕过既有 workflow 或权限规则

请求人工判断时必须说明：现状、选项、各自代价、agent 的建议。不要用"需要进一步确认"结束。

---

## 沙箱建议

如果执行环境支持沙箱，建议按角色递进：

- tester：只读挂载
- planner / reviewer / designer：读写文档目录，代码目录只读
- frontend / backend：读写代码目录，memory 限追加
- 所有角色：默认无网络，外发类操作一律走人工确认

没有沙箱时，用本文件 + review 收口替代，并在 `RUNS.md` 中记录是否发生过越权。

---

## 回写要求

- 每次越权或险些越权：写入 `05-memory/LESSONS.md`
- 每次权限模型变化：写入本文件 + `05-memory/EVOLUTION.md`
- 每次人工确认的高风险操作：写入当次报告，供 review 追溯

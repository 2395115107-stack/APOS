# Tech Stack

## 技术定位

APOS 当前首先是一个文档驱动的 AI 协作系统。

当前阶段不绑定具体前端或后端框架。技术栈约束重点是：

- 文件结构稳定
- Markdown 可读可维护
- agent 可按固定路径读取上下文
- 所有重要状态可追踪

## 当前技术形态

- 文档格式：Markdown
- 调度单位：workflow 文件
- 执行单位：agent 文件
- 状态记录：`02-product/TASKS.md`
- 决策记录：`05-memory/DECISIONS.md`
- 经验记录：`05-memory/LESSONS.md`
- 模式记录：`05-memory/PATTERNS.md`

## 工程原则

### 1. 路径稳定

不要频繁移动核心目录。

核心路径：

- `01-core/`
- `02-product/`
- `03-design/`
- `04-development/`
- `05-memory/`
- `07-workflows/`
- `08-agents/`

### 2. 文档即接口

每个 workflow 和 agent 都通过文件交接。

标准字段：

```text
Owner
Next
Inputs
Outputs
Skills
Writeback
```

### 3. 外部文档必须查新

涉及库、框架、SDK、云服务、CLI 时，优先使用文档查询类 skill。

推荐：

- `context7-mcp`
- `context7-cli`

### 4. 实现必须可验证

任何代码层改动都应说明：

- 如何运行
- 如何测试
- 风险在哪里
- 是否需要 reviewer / tester

## 后续技术栈扩展

如果 APOS 发展为实际应用，可以在这里补充：

- 前端框架
- 后端框架
- 数据库
- 部署方式
- 测试工具
- 代码规范

## 技术决策回写

任何长期技术决策都必须记录到：

- `05-memory/DECISIONS.md`

任何技术踩坑都必须记录到：

- `05-memory/LESSONS.md`

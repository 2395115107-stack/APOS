# Design System

## 设计定位

APOS 的设计系统首先服务“清晰协作”，其次才是视觉风格。

所有界面和文档设计都应优先满足：

- 信息层级清楚
- 状态可扫描
- 角色边界明确
- 操作路径短
- 长时间使用不疲劳

## 基础原则

### 1. 产品感优先

APOS 是开发系统，不是展示模板。

设计应偏向：

- 克制
- 清晰
- 可操作
- 适合重复使用

### 2. 信息密度适中

不要把每个区块都做成解释型大段落。

优先使用：

- 状态块
- 表格
- owner / next / inputs / outputs
- 简短判断
- 可复用模板

### 3. 视觉服务调度

UI 或文档结构必须让人快速知道：

- 当前是什么任务
- 谁负责
- 下一步是谁
- 输入是什么
- 输出是什么
- 要回写哪里

## 推荐文档结构

涉及任务和流程的文档，优先使用：

```text
目标
输入
流程
Owner
Next
Outputs
Skills
Writeback
验收标准
```

## 设计类 agent 使用规则

- `designer` 负责体验结构和视觉方向
- `frontend` 负责实现
- `tester-layout` 检查结构和布局
- `tester-quality` 检查视觉完成度
- `tester-accessibility` 检查可访问性

## 可复用模式

可复用的设计模式必须写入：

- `05-memory/PATTERNS.md`

设计问题和踩坑必须写入：

- `05-memory/LESSONS.md`

# Tools

## 说明

`09-tools/` 存放 APOS 的机械检查脚本，对应缺口分析 Gap 6（enforce invariants mechanically）。

## 当前脚本

- `check_docs.py`：文档完整性与引用一致性检查

## 使用

```text
python 09-tools/check_docs.py
```

退出码 0 = 通过，1 = 有问题。每次 release 前、memory-review 时、以及文档批量修改后运行。

## 新增脚本约定

- 只用 Python 标准库，不引入依赖
- 每个脚本在输出末尾给出 PASS / FAIL 和问题计数
- 脚本自身的变更走 `05-memory/EVOLUTION.md` 记录

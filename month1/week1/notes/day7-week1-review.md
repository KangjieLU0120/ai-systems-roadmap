# Day 7 - Week 1 Review / 第一周复盘

## 1. Goal / 今日目标

Today I reviewed the first week and upgraded the Python CLI file counter.

今天我复盘了第一周的学习内容，并升级了 Python 命令行文件统计工具。

## 2. Week 1 Summary / 第一周总结

This week I learned:

- Linux basic commands
- Git local workflow
- GitHub remote workflow
- VS Code with WSL
- Python script execution
- Python CLI tools
- Basic debugging

这一周我学习了：

- Linux 基础命令
- Git 本地工作流
- GitHub 远程仓库流程
- VS Code 连接 WSL 项目
- Python 脚本运行
- Python 命令行工具
- 基础 Debug 方法

## 3. Code Upgrade / 代码升级

I upgraded `scripts/file_counter.py` by adding:

- `DEFAULT_EXCLUDED_DIRS`
- `should_skip_path()`
- `--include-hidden`

我升级了 `scripts/file_counter.py`，让它可以默认跳过 `.git`、`.venv`、`__pycache__` 等目录，并支持通过 `--include-hidden` 参数统计隐藏目录。

## 4. Commands Used / 使用命令

```bash
python3 scripts/file_counter.py .
python3 scripts/file_counter.py . --include-hidden
python3 scripts/file_counter.py scripts
python3 scripts/file_counter.py month1
python3 scripts/file_counter.py --help
```

## 5. Key Concepts / 核心概念

### Default Behavior / 默认行为

A good tool should have a reasonable default behavior.

一个好的工具应该有合理的默认行为。

For this script, the default behavior is to skip tool-generated directories such as `.git`, `.venv`, and `__pycache__`.

对于这个脚本来说，默认行为是跳过 `.git`、`.venv`、`__pycache__` 等工具生成目录。

### Optional Argument / 可选参数

`--include-hidden` is an optional argument.

`--include-hidden` 是一个可选参数。

If I do not add it, hidden and cache directories are skipped.

如果不加这个参数，隐藏目录和缓存目录会被跳过。

If I add it, the script includes them.

如果加上这个参数，脚本会把它们也统计进去。

### Function Extraction / 函数拆分

I moved skip logic into `should_skip_path()`.

我把“是否跳过路径”的逻辑拆到了 `should_skip_path()` 函数中。

This makes the main scan loop easier to read.

这样主扫描流程更容易阅读。

## 6. Reflection / 今日思考

Before this week, I used tools separately. Now I can connect them into a workflow.

这一周之前，我只是分散地使用工具。现在我开始能把它们串成一个完整工作流。

The workflow is:

```text
open project -> write code -> run code -> debug -> write notes -> commit -> push
```

对应到实际命令是：

```bash
code .
python3 scripts/file_counter.py .
git status
git diff
git add .
git commit -m "..."
git push
```

This is the beginning of real engineering practice.

这是工程实践的开始。

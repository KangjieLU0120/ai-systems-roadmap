# Day 6 - Python CLI File Counter / Python 命令行文件统计工具

## 1. Goal / 今日目标

Today I built a small Python command-line tool to scan a directory and count files, folders, file extensions, and total size.

今天我完成了一个 Python 命令行工具，用来扫描目录，并统计文件数量、文件夹数量、文件后缀分布和总大小。

## 2. File Created / 创建文件

```bash
scripts/file_counter.py
```

## 3. Commands Used / 使用命令

```bash
python3 scripts/file_counter.py .
python3 scripts/file_counter.py month1
python3 scripts/file_counter.py scripts
```

## 4. Key Concepts / 核心概念

### pathlib.Path

`pathlib.Path` allows me to work with file paths as objects instead of plain strings.

`pathlib.Path` 可以让我用对象的方式处理文件路径，而不是只把路径当成普通字符串。

Examples:

```python
root.exists()
root.is_dir()
path.is_file()
path.suffix
path.parts
```

### argparse

`argparse` is used to receive command-line arguments.

`argparse` 用来接收命令行参数。

For example:

```bash
python3 scripts/file_counter.py .
```

The `.` is passed into the program as the `path` argument.

这里的 `.` 会作为路径参数传入程序。

### rglob

`root.rglob("*")` recursively scans all files and folders under the root directory.

`root.rglob("*")` 会递归扫描指定目录下的所有文件和文件夹。

### .git Directory / .git 目录

When I scanned the project root with `.`, the script also scanned the `.git` directory.

当我扫描项目根目录 `.` 时，脚本也会扫描 `.git` 目录。

`.git` contains Git internal files, so the first result showed many `.sample` files and files with no extension.

`.git` 里面有很多 Git 内部文件，所以第一次结果中出现了很多 `.sample` 文件和没有后缀的文件。

To make the result closer to real project files, I added this check:

```python
if ".git" in path.parts:
    continue
```

This skips files inside the `.git` directory.

这行代码会跳过 `.git` 目录里的文件。

### TypedDict

At first, I wrote:

```python
def scan_directory(root: Path) -> dict:
```

The code could run, but Pylance showed type warnings because `dict` did not specify key and value types.

代码可以运行，但 Pylance 会提示类型不够明确，因为 `dict` 没有说明 key 和 value 的类型。

Then I used `TypedDict`:

```python
class ScanResult(TypedDict):
    root: Path
    file_count: int
    directory_count: int
    total_size: int
    extension_counts: dict[str, int]
```

This makes the return type clearer.

这样可以让函数返回值的结构更清楚。

## 5. Debug Notes / Debug 记录

This script requires a command-line argument.

这个脚本需要命令行参数。

Correct command:

```bash
python3 scripts/file_counter.py .
```

If I press F5 directly without passing arguments, the program may report:

```text
the following arguments are required: path
```

This is not a code bug. It means the script did not receive the required path argument.

这不是代码错误，而是因为程序没有收到必须的路径参数。

Useful variables to observe during debugging:

```python
args.path
root
path
file_count
directory_count
total_size
extension_counts
result
```

## 6. My Reflection / 今日思考

Before Day06, I mainly ran simple Python scripts. Today I built a small but real command-line tool.

Day06 之前，我主要只是运行简单 Python 脚本。今天我完成了一个小但真实的命令行工具。

The most important idea is that engineering scripts should not hard-code everything. They should receive input, validate input, process data, and print clear output.

最重要的理解是：工程脚本不应该把所有内容写死，而应该能接收输入、检查输入、处理数据，并输出清晰结果。

I also learned that code can run successfully while still having type warnings in VS Code.

我也学到：代码可以成功运行，但 VS Code 仍然可能有类型提示警告。

Runtime errors and type checker warnings are different things.

运行时错误和类型检查警告是两类不同的问题。

## 7. Standard Workflow / 标准流程

```bash
cd ~/projects/ai-systems-roadmap

python3 scripts/file_counter.py .

git status
git diff

git add .
git commit -m "add day6 python file counter"
git push

git status
```

## 8. Day06 最新验收命令

完成代码和笔记后，执行：

```bash
cd ~/projects/ai-systems-roadmap

python3 scripts/file_counter.py .
python3 scripts/file_counter.py month1
python3 scripts/file_counter.py scripts
```

你应该看到程序正常输出统计结果。

然后检查 Git 状态：

```bash
git status
git diff
```

确认变化包括：

```text
scripts/file_counter.py
month1/week1/notes/day6-python-cli.md
```

如果你也配置了 VS Code Debug，可能还会有：

```text
.vscode/launch.json
```

`.vscode/launch.json` 可以提交，它是项目调试配置。

## 9. 提交到 GitHub

确认没问题后：

```bash
git add .
git commit -m "add day6 python file counter"
git push
git status
```

最终理想状态：

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Day06 到这里就合格了。你今天不是只写了一个统计脚本，而是第一次接触了“工程脚本”的基本形态：参数输入、路径处理、目录遍历、结果汇总、类型提示、Debug 验证。

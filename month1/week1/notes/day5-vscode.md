# Day 5 - VS Code Engineering Workflow / VS Code 工程使用

## 1. Goal / 今日目标

Today I learned how to use VS Code as an engineering IDE inside WSL.

今天我学习了如何在 WSL 环境中使用 VS Code 进行工程开发，包括打开项目、运行 Python、Debug、设置断点和查看变量。

## 2. Tools / 使用工具

- VS Code
- WSL: Ubuntu
- Python extension
- Pylance
- GitLens
- Error Lens
- Integrated Terminal

## 3. File Created / 创建的文件

```bash
scripts/hello.py
```

## 4. Program / 程序内容

```python
def build_message(name: str) -> str:
    message = f"Hello, {name}!"
    return message


def main():
    name = input("Your name: ")
    greeting = build_message(name)
    print(greeting)


if __name__ == "__main__":
    main()
```

## 5. Commands Used / 使用的命令

```bash
cd ~/projects/ai-systems-roadmap
mkdir -p scripts
python3 scripts/hello.py
code .
```

## 6. Debug Concepts / Debug 概念

### Breakpoint / 断点

A breakpoint pauses the program at a specific line.

断点可以让程序在某一行暂停，方便我观察程序状态。

### Step Over / 单步执行

Step Over runs the current line and moves to the next line.

单步执行可以让我一行一行观察程序如何运行。

### Variables / 变量窗口

The Variables panel shows the current values of variables.

变量窗口可以显示当前程序中变量的值，比如 `name`、`message` 和 `greeting`。

## 7. My Reflection / 今日思考

Before today, I mainly used VS Code as a text editor. Today I started using it as an engineering tool.

今天之前，我更多只是把 VS Code 当作文本编辑器。今天开始，我学习了如何把它作为工程开发工具使用。

The most important habit is to always know three things:

最重要的习惯是随时确认三件事：

1. Which project am I working in? / 我现在在哪个项目里？
2. Which Python interpreter am I using? / 我现在使用的是哪个 Python 解释器？
3. Can I run and debug the code? / 我能否运行和调试代码？

## 8. Standard Workflow / 标准流程

```bash
cd ~/projects/ai-systems-roadmap
code .
python3 scripts/hello.py
git status
git add .
git commit -m "add day5 vscode workflow notes"
git push
```

---

## 11. Day05 验收命令

完成后，在 WSL 里执行：

```bash
cd ~/projects/ai-systems-roadmap
python3 scripts/hello.py
git status
```

你应该能做到：

1. VS Code 能打开 WSL 项目
2. `hello.py` 能运行
3. 能设置断点
4. 能 F5 Debug
5. 能看到变量 `name` / `greeting` / `message`
6. `day5-vscode.md` 已完成

## 12. 提交到 GitHub

确认文件没问题：

```bash
git status
git diff
```

然后提交：

```bash
git add .
git commit -m "add day5 vscode workflow notes"
git push
git status
```

如果 `git push` 提示：

```text
Username for 'https://github.com':
Password for 'https://...':
```

这里的 Password 仍然是：

```text
GitHub Personal Access Token
```

不是 Linux 密码，也不是 GitHub 登录密码。

## 13. Day05 通过标准

最终执行：

```bash
git status
git log --oneline --decorate -5
```

理想状态：

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

并且 GitHub 页面能看到：

```text
scripts/hello.py
month1/week1/notes/day5-vscode.md
```

到这里，Day05 就通过。

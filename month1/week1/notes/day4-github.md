# Day 4 - GitHub Connection / GitHub 远程连接

## 1. Goal / 今日目标

今天的目标是把本地 Git 仓库（Local Repository）连接到 GitHub 上的远程仓库（Remote Repository），并把本地提交（Commit）推送（Push）到 GitHub。

The goal of Day 4 was to connect the local Git repository to a remote GitHub repository and push local commits to GitHub.

在 Day 4 之前，我已经学会了 `git commit`，但 `git commit` 只会把更改保存到本地仓库（Local Repository）。这些提交（Commits）保存在项目目录里的 `.git` 文件夹中。

Before Day 4, `git commit` only saved changes locally. The commits were stored in the local `.git` directory.

GitHub 不会自动看到本地代码。只有当 `git push` 成功完成后，GitHub 上的远程仓库（Remote Repository）才会显示这些代码和提交历史。

GitHub would not show the code until `git push` was successfully completed.

## 2. Commands Learned / 今天学习的命令

| Command | 中文解释 | English Explanation |
| --- | --- | --- |
| `git remote -v` | 查看当前本地仓库连接的远程仓库地址。 | Shows the remote repository URLs connected to the local repository. |
| `git remote add origin <remote-url>` | 添加一个名为 `origin` 的远程仓库地址。 | Adds a remote repository URL named `origin`. |
| `git remote set-url origin <remote-url>` | 修改已有的 `origin` 远程仓库地址。 | Updates the URL of the existing `origin` remote. |
| `git branch -M main` | 把当前分支重命名为 `main`。 | Renames the current branch to `main`. |
| `git push -u origin main` | 把本地 `main` 分支推送到 `origin`，并建立追踪关系（upstream）。 | Pushes local `main` to `origin` and sets the upstream tracking relationship. |
| `git status` | 查看工作区、暂存区、本地分支和远程分支的状态。 | Shows the state of the working directory, staging area, local branch, and remote tracking branch. |
| `git log --oneline --decorate` | 用简短格式查看提交历史，并显示分支和远程引用。 | Shows commit history in a short format with branch and remote references. |

## 3. What I Did Today / 今日操作流程

今天的实际流程是：

1. 确认本地仓库是干净的（clean working tree）。
2. 确认本地已经存在提交历史（local commits）。
3. 添加 GitHub 远程仓库（remote repository）。
4. 检查远程仓库地址（remote URL）。
5. 把本地 `main` 分支推送到 GitHub。
6. 确认本地 `main` 已经和远程 `origin/main` 同步。

添加远程仓库的命令是：

```bash
git remote add origin https://github.com/KangjieLU0120/ai-systems-roadmap.git
```

检查远程地址：

```bash
git remote -v
```

推送本地分支：

```bash
git push -u origin main
```

最后检查状态：

```bash
git status
```

最终成功的状态是：

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

这说明本地分支 `main` 和 GitHub 上的远程分支 `origin/main` 已经同步。

This means the local `main` branch is synchronized with the remote `origin/main` branch.

## 4. Problems Encountered / 遇到的问题

### 4.1 SSH connection failed / SSH 连接失败

执行下面的命令时：

```bash
ssh -T git@github.com
```

出现了这个错误：

```text
kex_exchange_identification: read: Connection reset by peer
Connection reset by 20.205.243.166 port 22
```

之后尝试通过 443 端口连接 SSH：

```bash
ssh -T -p 443 git@ssh.github.com
```

也失败了：

```text
Connection reset by 20.205.243.160 port 443
```

这说明问题很可能出现在网络层、代理、防火墙或当前网络环境，而不是本地 Git 仓库或 commit 本身。

This was likely a network-level issue, not a problem with the local Git repository or commit history.

### 4.2 HTTPS password authentication failed / HTTPS 密码认证失败

执行推送命令时：

```bash
git push -u origin main
```

Git 要求输入 username 和 password。

当时输入的用户名是：

```text
KangjieLU0120
```

但是密码认证失败：

```text
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed
```

GitHub 不再支持使用普通账号密码进行 Git HTTPS 操作。HTTPS 推送需要使用 Personal Access Token 或 GitHub CLI 认证。

GitHub no longer supports normal account password authentication for Git operations over HTTPS. A Personal Access Token or GitHub CLI authentication is required.

### 4.3 GitHub CLI issue / GitHub CLI 登录异常

尝试执行 `gh auth login`，但终端异常显示：

```text
gzip: stdin: not in gzip format
```

这不是标准的 GitHub CLI 登录流程。遇到这种异常时，最安全的方式是关闭终端、重新进入 WSL、检查 `git status` 和远程状态，而不是继续乱按 Enter。

This was not part of the standard GitHub CLI login flow. When this happens, it is safer to restart the terminal and verify the Git repository state before continuing.

## 5. Key Concepts / 核心概念

### Local Repository / 本地仓库

本地仓库是保存在自己电脑上的 Git 仓库，commit 历史保存在项目目录下的 `.git` 文件夹中。

A local repository is a Git repository stored on my own machine. Its commit history is stored inside the `.git` directory.

### Remote Repository / 远程仓库

远程仓库是托管在 GitHub 上的仓库，用于备份、展示、协作和同步代码。

A remote repository is hosted on GitHub and is used for backup, sharing, collaboration, and synchronization.

### origin

`origin` 是远程仓库地址的默认别名。它不是 GitHub 用户名，也不是特殊账号。

`origin` is the default nickname for the remote repository URL. It is not a GitHub username or a special account.

### main

`main` 是当前项目的主分支。

`main` is the main branch of this project.

### git push

`git push` 会把本地 commit 上传到远程仓库。

`git push` uploads local commits to the remote repository.

### -u / upstream

`-u` 会建立本地 `main` 和远程 `origin/main` 的追踪关系。设置成功后，以后通常只需要执行 `git push`。

The `-u` option sets the upstream tracking relationship between local `main` and remote `origin/main`. After that, future pushes can usually use only `git push`.

## 6. Reflection / 今日思考

我之前以为 `git commit` 后 GitHub 就能看到代码，但实际上 commit 只保存在本地（local）。GitHub 看不到代码，是因为还没有执行 `git push`。

`git remote` 的作用是把本地仓库（Local Repository）和 GitHub 远程仓库（Remote Repository）连接起来。`git push` 才是真正把 commit 上传到 GitHub 的动作。

SSH、HTTPS、Token、GitHub CLI 这些认证问题，和本地 Git 历史是两类问题。认证失败不一定说明 commit 丢了，也不一定说明本地仓库坏了。

Debug Git 问题时，不应该慌，应该先检查：

```bash
git status
git log --oneline --decorate
git remote -v
```

如果 `git status` 显示：

```text
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

说明本地和远程已经同步。

## 7. Standard GitHub Workflow / 之后提交到 GitHub 的标准流程

标准流程：

```bash
cd ~/projects/ai-systems-roadmap

git status

git diff

git add .

git status

git commit -m "write clear commit message"

git push

git status

git log --oneline --decorate -5
```

步骤说明：

| Step | 中文解释 | English Explanation |
| --- | --- | --- |
| `cd ~/projects/ai-systems-roadmap` | 进入项目目录。 | Enter the project directory. |
| `git status` | 查看当前有哪些文件被修改、新增或暂存。 | Check which files are modified, new, or staged. |
| `git diff` | 查看还没有暂存的具体改动内容。 | Review unstaged changes before staging them. |
| `git add .` | 把当前目录下的改动加入暂存区（staging area）。 | Add changes under the current directory to the staging area. |
| `git status` | 再次确认哪些改动已经进入暂存区。 | Confirm which changes are now staged. |
| `git commit -m "write clear commit message"` | 创建一次提交，并写清楚本次改动。 | Create a commit with a clear message describing the change. |
| `git push` | 把本地 commit 推送到 GitHub 远程仓库。 | Push local commits to the GitHub remote repository. |
| `git status` | 确认推送后的本地状态是否干净、是否和远程同步。 | Confirm the repository is clean and synchronized after pushing. |
| `git log --oneline --decorate -5` | 查看最近 5 条提交和分支位置。 | Show the latest 5 commits with branch labels. |

不要在没有检查 `git status` 和 `git diff` 的情况下直接 `git add .` 和 `git commit`。提交信息应该具体描述本次改动。

Do not run `git add .` and `git commit` blindly without checking `git status` and `git diff`. Commit messages should clearly describe the actual change.

## 8. Good Commit Message Examples / 好的提交信息示例

好的提交信息：

```bash
git commit -m "add day4 github connection notes"
git commit -m "update week1 readme"
git commit -m "add linux command practice notes"
git commit -m "fix github remote configuration"
```

不好的提交信息：

```bash
git commit -m "update"
git commit -m "test"
git commit -m "123"
```

好的提交信息更具体，可以让自己和别人快速看懂这次 commit 做了什么。例如 `add day4 github connection notes` 一眼就能看出是添加 Day 4 的 GitHub 连接笔记；而 `update`、`test`、`123` 太模糊，之后查看历史时很难判断改动内容。

## 9. Security Notes / 安全注意事项

不要把 GitHub token 写进 Markdown 文件。

Do not write GitHub tokens into Markdown files.

不要把密码、私钥或 token 上传到 GitHub。

Do not upload passwords, private keys, or tokens to GitHub.

`id_ed25519` 是私钥（private key），不能分享，也不能上传到公开仓库。

`id_ed25519` is a private key and must not be shared or uploaded to a public repository.

`id_ed25519.pub` 是公钥（public key），可以添加到 GitHub。

`id_ed25519.pub` is a public key and can be added to GitHub.

如果 token 泄露，应该立刻在 GitHub settings 中撤销（revoke）它。

If a token is leaked, revoke it immediately in GitHub settings.

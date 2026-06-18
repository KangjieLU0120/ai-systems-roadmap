# Day 2 - Linux Basic Commands

## 1. Commands I learned today

### pwd

`pwd` means print working directory.

It shows the current directory I am in.

Example:

```bash
pwd
```

### ls

`ls` lists files and folders in the current directory.

Common usage:

```bash
ls
ls -l
ls -a
ls -la
```

### cd

`cd` changes the current directory.

Examples:

```bash
cd month1/week1
cd ..
cd ~
```

### mkdir

`mkdir` creates directories.

Examples:

```bash
mkdir notes
mkdir -p month1/week1/notes
```

### touch

`touch` creates an empty file.

Example:

```bash
touch notes/linux-basic.md
```

### cat

`cat` shows file content.

Example:

```bash
cat notes/linux-basic.md
```

### cp

`cp` copies files or directories.

Examples:

```bash
cp a.txt b.txt
cp -r folder1 folder2
```

### mv

`mv` moves or renames files.

Examples:

```bash
mv old.txt new.txt
mv file.txt experiments/
```

### rm

`rm` removes files.

Examples:

```bash
rm file.txt
rm -r folder
```

Be careful: files removed by `rm` usually do not go to the recycle bin.

### find

`find` searches files by name or type.

Examples:

```bash
find . -name "*.md"
find . -type f
find . -type d
```

### grep

`grep` searches text inside files.

Examples:

```bash
grep "keyword" file.txt
grep -n "keyword" file.txt
grep -rn "keyword" .
```

### Why `find .` is not alphabetical

`find .` recursively walks through the directory tree. It prints paths in the order returned by the filesystem, not necessarily alphabetical order.

If I want alphabetical order, I can use:

```bash
find . | sort
```

`ls` is usually sorted by default, but `find` is mainly used for recursive searching, so I should not rely on its output order.

The key idea is: `find` is a traversal tool, not a sorted display tool.

## 2. Confusing commands

### cp vs mv

`cp` copies a file, so the original file still exists.

`mv` moves or renames a file, so the original path disappears.

### find vs grep

`find` searches by file name.

`grep` searches inside file content.

### `>` vs `>>`

`>` overwrites a file.

`>>` appends content to a file.

### `.` vs `..`

`.` means current directory.

`..` means parent directory.

## 3. Relative path vs absolute path

An absolute path starts from `/`.

Example:

```text
/home/kangjielu/projects/ai-systems-roadmap/month1/week1/notes/linux-basic.md
```

A relative path starts from the current directory.

Example:

```text
notes/linux-basic.md
```

If I am currently in:

```text
/home/kangjielu/projects/ai-systems-roadmap/month1/week1
```

then:

```text
notes/linux-basic.md
```

means:

```text
/home/kangjielu/projects/ai-systems-roadmap/month1/week1/notes/linux-basic.md
```

## 4. My Day 2 takeaway

Today I learned how to create, view, move, copy, delete, and search files in Linux. The most important habit is to always use `pwd` to confirm where I am before running commands.

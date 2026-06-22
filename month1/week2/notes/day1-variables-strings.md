# Week 2 Day 1 - Variables, Strings, Input and Output / 变量、字符串、输入输出

## 1. Goal / 今日目标

Today I learned basic Python variables, strings, input, output, f-strings, and simple function encapsulation.

今天我学习了 Python 的变量、字符串、输入输出、f-string，以及简单的函数封装。

## 2. File Created / 创建文件

```bash
month1/week2/exercises/day1_personal_info.py
```

## 3. Commands Used / 使用命令

```bash
cd ~/projects/ai-systems-roadmap
python3 month1/week2/exercises/day1_personal_info.py
```

## 4. Key Concepts / 核心概念

### Variable / 变量

A variable gives a name to a value.

变量是给数据起名字。

```python
name = "Kangjie"
```

### String / 字符串

A string is text data wrapped by quotes.

字符串是被引号包住的文本数据。

```python
school = "PolyU"
```

### input

`input()` receives user input from the terminal.

`input()` 用来从终端接收用户输入。

### print

`print()` displays output in the terminal.

`print()` 用来在终端输出内容。

### f-string

An f-string inserts variables into a string.

f-string 可以把变量插入字符串中。

```python
intro = f"My name is {name}."
```

### Function / 函数

A function wraps a piece of logic and makes code easier to reuse.

函数可以封装一段逻辑，让代码更容易复用。

## 5. Reflection / 今日思考

Today I learned that a small program should still have structure.

今天我学到，即使是一个很小的程序，也应该有结构。

The basic structure is:

```text
input -> process -> output
```

对应到今天的程序：

```text
input user information -> build introduction -> print introduction
```

Using a function makes the code cleaner and easier to change.

使用函数可以让代码更清晰，也更容易修改。

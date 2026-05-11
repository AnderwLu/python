# Python基本语法文档实现计划

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 编写一篇面向有编程基础同学的Python基本语法速查表文档

**架构：** 采用速查表风格，分节罗列Python核心语法点和代码示例，保持极简

**Tech Stack:** Markdown

---

### Task 1: 编写文档框架和注释部分

**Files:**
- Create: `03. python基本语法/课件.md`

**Step 1: 编写文档标题和注释部分**

写入内容：
- 文档标题
- 单行注释 `#`
- 多行注释 `"""` / `'''`
- 文档字符串

**Step 2: 验证文件创建**

运行: `cat "03. python基本语法/课件.md"`
预期: 文件包含注释相关内容

**Step 3: Commit**

```bash
git add "03. python基本语法/课件.md"
git commit -m "docs: 添加Python基本语法文档框架和注释部分"
```

---

### Task 2: 添加变量与基本数据类型

**Files:**
- Modify: `03. python基本语法/课件.md`

**Step 1: 添加变量与赋值**

追加内容：
- 变量命名规则
- 动态类型赋值
- 多重赋值

**Step 2: 添加基本数据类型**

追加内容：
- 整数、浮点数
- 字符串（引号、转义、格式化）
- 布尔值
- None

**Step 3: Commit**

```bash
git add "03. python基本语法/课件.md"
git commit -m "docs: 添加变量与基本数据类型"
```

---

### Task 3: 添加数据结构

**Files:**
- Modify: `03. python基本语法/课件.md`

**Step 1: 添加列表**

追加内容：
- 定义、索引、切片
- 常用方法（append, extend, insert, remove, pop）

**Step 2: 添加字典**

追加内容：
- 定义、访问、修改
- 常用方法（keys, values, items, get）

**Step 3: 添加元组和集合**

追加内容：
- 元组（不可变列表）
- 集合（去重、交集、并集）

**Step 4: Commit**

```bash
git add "03. python基本语法/课件.md"
git commit -m "docs: 添加数据结构"
```

---

### Task 4: 添加运算符和输入输出

**Files:**
- Modify: `03. python基本语法/课件.md`

**Step 1: 添加运算符**

追加内容：
- 算术运算符
- 比较运算符
- 逻辑运算符
- 成员/身份运算符

**Step 2: 添加输入输出**

追加内容：
- print() 输出
- input() 输入
- f-string 格式化

**Step 3: Commit**

```bash
git add "03. python基本语法/课件.md"
git commit -m "docs: 添加运算符和输入输出"
```

---

### Task 5: 添加控制流和函数

**Files:**
- Modify: `03. python基本语法/课件.md`

**Step 1: 添加条件语句**

追加内容：
- if / elif / else
- 三元表达式

**Step 2: 添加循环语句**

追加内容：
- for 循环（遍历、range）
- while 循环
- break / continue
- 列表推导式

**Step 3: 添加函数定义**

追加内容：
- def / return
- 参数（位置、默认、关键字、*args, **kwargs）
- lambda 表达式

**Step 4: Commit**

```bash
git add "03. python基本语法/课件.md"
git commit -m "docs: 添加控制流和函数"
```

---

### Task 6: 最终检查

**Files:**
- Read: `03. python基本语法/课件.md`

**Step 1: 检查文档完整性**

运行: `wc -l "03. python基本语法/课件.md"`
预期: 文档行数合理，结构完整

**Step 2: 检查格式**

运行: `cat "03. python基本语法/课件.md"`
预期: Markdown格式正确，代码块语法高亮

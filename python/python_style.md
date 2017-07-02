# Python Style

#### Lint

#### 导入

- import module ／ import package
- from package import module
- from package_one.package_two import module
- import package_one.package_two.module
- from package import long_module_name as module
- 不要使用相对导入
- 不要 import os, sys (分开两行)
- 应该位于 模块注释／文档字符串 和 全局变量／常量 之间
- 顺序
  - 标准库 > 第三方库 > 程序内部
  - 按完整路径、a-z排序

#### 异常

- 使用 except Error as error: 不要用 ,
- 不要用 except: / except Exception: / except StandardError:
- try / except 中的代码块尽量小
- raise MyException('Error message') 这样的写法

#### 全局变量

#### 嵌套

#### 列表推导

- 我建议超过一个 for 或者超过一个 if 的逻辑循环都不要用列表推导

#### 迭代器

#### 生成器

- Google Style Guide 里面的评价是“没有缺点”，感受一下。

#### Lambda

#### 条件表达式

- x = 1 if condition else 2

#### 默认参数

- 鼓励使用, 也要记住YAGNI，但千万别使用可变对象
- 除非你故意要共享改变这一对象

#### 属性

#### 布尔

- 通常隐式判断更好，大部分情况下都语义明确，并且也更快。
- 除非：
  - 例如：If value is not None 需要指定判断

#### 过时的语言特性

#### 词法作用域

#### 装饰器

#### 线程

- 读 Queue / threading 模块

#### 屠龙刀

#### 行长

- <= 79

#### 括号

- 条件和返回语句中，不要使用括号
- 除非：可以作为多行续行的方法、元组

#### 缩进

- 别用 tab

- ```python3
  foo = long_function_name(var_one, var_two,
                           var_three, var_four)
  ```

- 如果一个逻辑需要多行，就要考虑下了。比如是不是有可以赋值为复用的变量等等

#### 空行

- 顶级之间空2行
- 类里面：第一个方法和类空1行，方法之间空1行

#### 空格

- 贴近() [] {}的字符不需要空格
- , : 只需要在后面加空格
- 运算符两边都要空格
- 关键字参数=两边不要空格
- 不要用空格来对齐行尾注释、字典冒号这类标记

#### Shebang

- 只有被直接执行的文件比如 main 才需要

- # ! /usr/bin/env python3

#### 注释

- 文档字符串 __doc__
  - 包、模块、类、函数的第一个注释

#### 类

- 显式继承 class SampleClass(object): 而且会默认增加

- ```python3
  __new__ __init__ __delattr__ __getattribute__ __setattr__ __hash__ __repr__ __str__
  ```

#### 字符串

- 如果不是刻意而为，不要用+，用%或者.format()

- ```python3
  # 循环中不要使用
  str += 'a'
  str = str + 'a'
  # 这样计算会很慢（why）
  # 可以先在循环中列表保存再在循环外合并
  items.append('{}'.format(str))
  ''.join(items)
  ```

- ```python3
  ('abcd'
   'efg')
  """
  abcd
  efg
  """
  # 前者更不容易破坏文件原有的缩进
  ```

#### 文件和sockets

- 使用 with .. as .. 语句，否则gc会很费解

- ```python3
  # 不支持 with 的
  import contextlib
  with contextlib.closing(urllib.urlopen("http://www.python.org/")) as front_page:
      for line in front_page:
          print line
  ```

#### TODO注释

- ```python3
  # TODO(zxy@gmail.com): something to do
  ```

#### 语句

- 应该独占一行

#### 访问控制

#### 命名

- module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name

- 避免：单字符、-、开头结尾都双下划线

- _module_variable / _module_function 在 from * 语句不会被导入

- __class_internal

- **Python之父Guido推荐的规范**

  | Type                       | Public             | Internal                                 |
  | -------------------------- | ------------------ | ---------------------------------------- |
  | Modules                    | lower_with_under   | _lower_with_under                        |
  | Packages                   | lower_with_under   |                                          |
  | Classes                    | CapWords           | _CapWords                                |
  | Exceptions                 | CapWords           |                                          |
  | Functions                  | lower_with_under() | _lower_with_under()                      |
  | Global/Class Constants     | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER                         |
  | Global/Class Variables     | lower_with_under   | _lower_with_under                        |
  | Instance Variables         | lower_with_under   | _lower_with_under (protected) or __lower_with_under (private) |
  | Method Names               | lower_with_under() | _lower_with_under() (protected) or __lower_with_under() (private) |
  | Function/Method Parameters | lower_with_under   |                                          |
  | Local Variables            | lower_with_under   |                                          |

#### main

- 如果文件需要作为脚本执行，就把执行放在 main() 中，并用

- ```python3
  if __name__ == '__main__':
      main()
  ```

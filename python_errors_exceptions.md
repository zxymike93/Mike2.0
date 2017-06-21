## Errors and Exceptions
> Python 中至少有两种不同的 error: syntax errors / exceptions.

### Syntax Errors - 语法错误
```python3
>>> while True print('Hello world')
  File "<stdin>", line 1  # 错误发生在哪个文件哪行
    while True print('Hello world')  # error 是在箭头前面发生的
                   ^
SyntaxError: invalid syntax
```

### Exceptions
> 语法错误之外的 error
```python3
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero  # 最后一行说明引发的 error 是什么
```
*这里有一个内置exception list: https://docs.python.org/3/library/exceptions.html#bltin-exceptions*

### Handling Exceptions
```python3
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
```
*假设是 except IndexError: 会由于捕捉不到,交给给默认异常处理向上传递.*
```python3
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

...D
...C
...B
# 如果顺序倒过来, 结果则是 B..B..B
```
```python3
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```
```python3
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
```python3
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
### Raising Exceptions
> raise 可以直接产生异常
```python3
>>> raise NameError('HiThere')  # 或者直接用类不用实例 NameError >> NameError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
在 try...except 中如果捕捉到异常又不想处理它,可以直接用 raise 重新引起.
```python3
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
```

### User-defined Exceptions
> 定义自己的异常类只需要继承 Exception
```python3
class Error(Exception):
    """一般会写一个父类, 并且命名为 Error"""
    pass


class InputError(Error):
    """输入错误

    属性:
        expression -- 引起错误的 input 语句
        message -- 错误信息
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
```

### Defining Clean-up Actions
> finally 子句在离开 try 语块的时候执行, 作为清理是很常用的.
```pythone
try:
    f = open('hello.py', 'r')
except FileNotFoundError:
    ...
finally:
    f.close()
```

### predefined Clean-up Actions
> 比如 with 语句, 无论执行成功或失败, 都会 clean-up.
```python3
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

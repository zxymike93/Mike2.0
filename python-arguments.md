# 函数的参数

## 位置参数

```python
def fun(a, b, c):
    print(a, b, c)
    
>>> fun(1, 2, 3)
1 2 3
# 也可以用 name=value 的形式
>>> fun(c=1, b=4, a=5)
5 4 1
```

## 默认参数

```python
def power(x, n=2):
    print(x ** n)
    
>>> power(2)
4
# 可以通过位置传递
>>> power(2, 3)
8
# 可以通过 name=value 的形式传递，这时候不限位置
>>> power(2, n=3)
8
```

## 可变参数

```python
# 使用位置参数，那么在下面这个函数中
# 需要手动传入可迭代的对象
def loop(number):
    for n in number: print(n, end=' ')

>>> L = [1, 2, 3]
>>> loop(L)
1 2 3

# 使用可变参数
def loop(*number):
    for n in number: print(n, end=' ')
 
>>> loop(1, 2, 3)
1 2 3
>>> loop([12356], {'a':1, 'b': 2})
[12356], {'a':1, 'b': 2}
>>> loop('abc')
abc

# 调用时会自动以 tuple 类型传入
```

## 关键字参数

```python
def person(name, **kwargs):
    print(name, kwargs)
    
# 直接 k=v 调用，注意：key 会自动变为 str
# 或者传入 **some_dict
>>> person('mike', job='programmer')
mike {'job': 'programmer'}
>>> me = {'job': 'programmer', 'home': 'gz'}
>>> person('mike', **me)
mike {'job': 'programmer', 'home': 'zj'}
```

## keyword-only参数

```python
def person(name, *, job, home):
    print(name, job, home)
    
>>> person('mike', job='programmer', home='gz')
mike {'job': 'programmer', 'home': 'zj'}
# 咋一看和关键字参数有点类似
# 实际上，调用必须根据给定的 name=value 形式

# keyword-only 也可以提供默认值
# 不过如上所述，必须通过 name=value 的方式传参
def person(name, *args, job='programmer', home):
    print(name, args, job, home)
    
>>> person('mike', 1, 2, 3, home='gz')
mike (1, 2, 3) programmer gz
```

## 顺序

### 定义函数时用的顺序

> 位置参数 — 默认参数 — 可变参数 — 命名关键字参数 — 关键字参数

```python
def fun(pos1, pos2, defa1=None, defa2=True *args, name1, name2='abc', name3, **kwargs)
```

### 调用函数时用的顺序

> 调用的顺序不能用上面的顺序来记
>
> 传参的写法如下：

```python
fun(pos, name=value, *sequence, **dictionary)
```

> 根据上述写法，python 寻找参数过程大概为：
>
> 1. 从左到右，先给位置参数赋值，这时候也可能会给默认参数赋值。
> 2. 根据 name，可能给位置参数、默认参数、keyword-only参数赋值。
> 3. 如果 position 或 name=value 有不能对应的位置参数、默认参数、kwonly参数，那么，如果 function 是接受 *args, **kwargs 的就会 collect 它们。否则，会出现 TypeError: …. but xxx were given.
> 4. *sequence, **dictionary 是在传参时解包，如何对应哪个形参赋值，也是遵循上述原则。
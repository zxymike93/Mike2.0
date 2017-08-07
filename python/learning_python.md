# Python 学习手册第四版 笔记

### Python 解释器

>  运行 Python 程序的程序. 整个 Python 程序运行过程为: 读取源码 .py > 编译为字节码 .pyc > PVM 运行

### UNIX 脚本 

> shell / Python 文件常常使用 `#! /usr/bin/env sh` 这样的开头. 如果文件具有 x 权限, 可以用 `./file.sh` 来执行脚本. 
>
> 实际上, 第一行是告诉操作系统到哪里寻找运行该脚本的解释器. 相当于执行了 `sh file.sh` .
>
> 另外, 打开 `/usr/bin/env` 可以看到, 实际上就是平常用来查看环境变量的 env 程序.
>
> 使用这个开头而不是硬编码的 `#! /usr/bin/python` 等于用 env 程序找到 python 程序的位置(一般查找 PATH 变量).

### 模块导入

> 上述 UNIX 脚本的方法使用在 Python 上也一样, `#! /usr/bin/env python` + 可执行权限 就可以直接运行, 而不必需添加 python 命令前缀. 
>
> 有趣的是, 就算文件不用 .py 后缀也一样遵循上述原则.
>
> 那么 .py 后缀有何用处呢?
>
> 其中一点是, 只有 .py 后缀的文件才能被当作 python 模块导入.
>
> 另外一提, 只有被导入过的 python 文件才会产生 .pyc 字节码文件. 

### Python 中的重载

> ```py
> #! python2
> import sample
> reload(sample)
>
> #! python3
> import sample
> from imp import reload
> reload(sample)
> ```
>
> import 是个开销很大的操作, 所以一个模块被导入之后只执行一次. reload 是为了解决运行过程中被导入的模块发生修改的情况. 
>
> 有两点值得注意: 1. Python 不支持函数重载; 2. 通过 `from .. import ..` 导入的模块不会被 reload 更新.


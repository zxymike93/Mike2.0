## 内建函数
- abs 绝对值
- all 如果iterable中所有元素为True，返回True. 空也返回True
- any 如果iterable中任一元素为True，返回True. 空则返回False
- bin 把int转为二进制形式
- bool 返回参数的布尔值
- bytearray
- bytes
- callable 判断一个对象是否可调用
- classmethod 相当于@classmethod
- complex
- delattr(x, 'foobar') 等同于 del x.foobar
- dict
- dir 返回属性列表
- divmod 返回(a // b, a % b)
- enumerate 枚举
- eval
- exec 执行代码对象
- filter(func, iterable)
  返回一个迭代器，包含对iterable执行func后返回True的元素。
- float
- format 字符串格式化
- frozenset
- getattr(obj, 'attr') 得到attribute的值，会向上寻找父类.
- globals 当前全局变量的一个字典
- hasattr 调用getattr判断是否存在一个属性，返回布尔值.
- hash 求哈希值
- help 查看文档字符串
- hex 将int转换为0x前缀的十六进制字符串
- id 对象的内存地址
- input 从stdin读取一行并转为字符串
- int
- isinstance(ins, class) 检查是否为实例, class可为元组
- issubclass(cls, class) 检查是否为子类, class可为元组
- iter 返回一个迭代器对象，参数必须有\_\_iter\_\_()或者\_\_getitem\_\_()
- len 求长度
- list
- locals
- map 返回一个迭代器，对iterable中的每个元素执行func
- max 求数组中最大值
- memoryview
- min 求数组中最小值
- next 调用\_\_next\_\_()从迭代器中检索下一项
- object
- oct 把int转换为八进制
- open 打开文件对象
- pow(x, y[, z]) x\*\*y [% z]
- print(obj, sep='', end='\n', file=sys.stdout, flush=False) 打印
- property
- range
- repr
- reversed
- round
- set
- setattr
- slice 切片
- sorted 排序
- staticmethod 相当于@staticmethod
- str
- sum 求数组和
- super
- tuple
- vars
- type
- zip
- \_\_import\_\_
- ascii
- ord
- chr
- compile

## 文字处理
- re
- readline
- textwrap

## 二进制数据
- struct

## 数据类型
- datetime
- collections
- copy
- pprint
- enum

## 数字和数学
- math
- random

## 函数编程
- itertools
- functools
- operator

### 文件与目录
- os.path
- fnmatch
- shutil

## 数据持久化
- pickle
- shelve
- dbm
- sqlite3

## 压缩和归档
- zlib
- gzip
- zipfile
- tarfile

## 文件格式
- csv
- configparser
- plistlib

## 加密
- hashlib

## 操作系统
- os
- io
- time
- argparse
- logging
- logging.config
- platform

## 并发
- threading
- subprocess
- queue

## 通信
- socket
- ssl
- select
- asyncio
- mmap

## 互联网
- email
- json
- mimetypes
- base64

## 结构化标记处理
- html
- xml

## 网络协议
- webbrowser
- cgi
- wsgiref
- urllib
- http
- smtplib
- socketserver

## 多媒体
- chunk

## 国际化
- locale

## 程序框架
- cmd

## tk图形用户接口
- tkinter

## 开发工具
- pydoc
- doctest
- unittest
- unittest.mock

## 调试
- pdb
- timeit

## 软件包装和发布
- venv
- distutils

## 运行时
- sys
- sysconfig
- builtins
- \_\_main\_\_
- warnings
- contextlib
- traceback
- \_\_future\_\_
- gc

## 自定义Python解释器

## 导入
- importlib

## 语言

## 杂
- formatter

## MS 专用

## Unix 专用
- tty
- pty
- fcntl
- pipes
- syslog

## 取代
- imp

## ...

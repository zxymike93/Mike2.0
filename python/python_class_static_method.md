# method, classmethod and staticmethod in Python

> 探讨三者的不同，以及应用场景。最后举出开源项目中的例子。

## 介绍三种方法

```py2
#! sample.py

class Foo(object):

    def foo(self, x):
        print 'executing foo(%s, %s)' % (self, x)
        
    @classmethod
    def class_foo(cls, x):
        print 'executing class_foo(%s, %s)' % (cls, x)
        
    @staticmethod
    def static_foo(x):
        print 'executing static_foo(%s)' % x
```

启动交互式解释器

```py2
>>> from sample import Foo
>>> Foo
<class 'sample.Foo'>
>>> f = Foo()
>>> f
<sample.Foo object at 0x7f2b3a00a7d0>
```

方法（也称实例方法 instance method）：

```py2
>>> f.foo(1)
executing foo(<sample.Foo object at 0x7f2b3a00a7d0>, 1)
# 隐性地传入 self 作为第一个参数
# 类似于 foo(self, 1)
# 如果 f.foo()
# TypeError: foo() takes exactly 2 arguments (1 given)
```

类方法

```py2
>>> f.class_foo(1)
executing class_foo(<class 'sample.Foo'>, 1)
>>> Foo.class_foo(1)
executing class_foo(<class 'sample.Foo'>, 1)
# 类似的，无论是 instance 调用，还是 cls 调用，类方法都把 cls 作为第一个参数
```

静态方法

```py2
>>> f.static_foo(1)
executing static_foo(1)
>>> Foo.static_foo(1)
executing static_foo(1)
＃ 如果 f.static_foo() or Foo.static_foo()
＃ TypeError: static_foo() takes exactly 1 argument (0 given)
＃ 可见，不需要 self / cls 作为隐性参数
＃ 只是调用方式为 instance.staticmethod() / class.staticmethod()
＃ 这样就根普通的函数类似，但可以归类到一个类里面
```

最后再看 method / classmethod / staticmethod 是如何绑定参数的，配合上面的 Error 来理解：

```py2
# method
>>> print f.foo
<bound method Foo.foo of <sample.Foo object at 0x7f2b3a00a7d0>>

# classmethod
>>> print f.class_foo
<bound method type.class_foo of <class 'sample.Foo'>>
>>> print Foo.class_foo
<bound method type.class_foo of <class 'sample.Foo'>>

# staticmethod 不绑定 instance / class
>>> print f.static_foo
<function static_foo at 0x7f2b3a0140c8>
>>> print Foo.static_foo
<function static_foo at 0x7f2b3a0140c8>
```


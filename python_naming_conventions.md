## 命名惯例

`_bar`

> from module import * 不会导入 _bar

`bar_`

> 为了避免和关键字冲突, 如: class_

`__bar`

> 作为类属性时, 实际上变成了 _Foo__bar

`__init__`

> 请按照官方文档的指导来使用

`小写的 l / 大写的 O / 大写的 I`

> 不要用作变量名, 可能会由于字体原因, 和数字 0 / 1 混淆

`mymodule 或者 module_name / mypackage`

> 模块和包都必须小写, 不建议使用下划线, 除非运用在模块名中能提高可读性

`ClassName`

`func 或者 func_name`

> 在某些情况, 比如: threading.py 中, 为了保持函数命名风格一致, 可采用 `getName` 这种 mixedCase 的方式.

- always 用 `self` 作为示例方法的第一个参数, `cls` 作为类方法的第一个参数. 如果**不得不**用到和保留字冲突的形参名, 使用 `type_` 这样的方式替代(比用 `ty` 好.)
- 常量通常定义在模块中(开头), 使用 `CONTENT_CHUNK_SIZE` 这样的全大写配合下划线的方式.

`实例变量 ins 或 new_cj / 方法名 info 或者 method_name`

> 实例变量和方法都遵循函数命名惯例, 如果是私有方法, 则用 _new_headers 这种前面多个下划线.
>
> 按照前面所说 __bar -> _Foo\_\_bar 的规则, 可以用此方式避免子类和基类方法名冲突.
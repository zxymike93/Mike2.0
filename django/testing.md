# Testing

- [编写运行测试](#编写运行测试)
- [测试工具](#测试工具)
- [测试话题](#测试话题)


## 编写运行测试

### write

用 Python 的 unittest 模块也是可以的，但如果依赖 Django 的 Models/Database，直接继承 `django.test.TestCase` 是非常方便的。

当使用 `python manage.py test` 时，命令会自动找到所有 test\*.py 中 TestCase 的子类来运行。

### run


## 测试工具

### Client

### 不同的 testcase 类

### 

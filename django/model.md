# Models and Databases
- Models
- Queries
- Aggregation
- Search
- Managers
- 裸SQL
- 事务
- 多DB
- TableSpaces
- Database access optimization
- Models之间关系的API

-----

## Models

### 字段选项
- null
- blank
> null是数据库的空值，blank是表单数据验证能否为空。
- choices
- default
- help_text
- primary_key
> 默认把自带的id作为pk
- unique

### 关系
- many-to-one
> fk = django.db.models.ForeignKey(ForeignModel)

- many-to-many
> many = django.db.models.ManyToManyField(ManyModel)
> 多对多在关联的两个模型中的任一个添加多对多Field都可以

- one-to-one
> 当某个对象想扩展自另一个对象时，最常用的方式就是在这个对象的主键上添加一对一关系。

### Meta
> 任何不是字段的数据

[Meta 的选项](https://docs.djangoproject.com/en/1.11/ref/models/options/)

### Model 的属性

model 最重要的属性就是 Manager，默认的叫做 `objects`。它是从数据库查询实例的接口，并且只能通过类调用，不能通过实例调用。

### Model 的方法

[Model 子类继承的方法](https://docs.djangoproject.com/en/1.11/ref/models/instances/#model-instance-methods)
，除此之外，还有一些方法是推荐使用者定义的：
- `__str__()  # python2中使用 __unicode__()`
- ```python
  get_absolute_url()
  # 例如
  class List(models.Model):
      [...]
      def get_absolute_url(self):
          return '/lists/%s' % self.id
  # 就可以在别的地方使用比如
  return redirect(list_ins)
  ```

另外，上面链接提到的继承的方法都是可以重写的，最典型的比如 save()

```python3
    def save(self, *args, **kwargs):
        do_something()
        super(Blog, self).save(*args, **kwargs)
```
-----

还有一个常见的需求是，在方法中使用 SQL 语句。[link](https://docs.djangoproject.com/en/1.11/topics/db/sql/)

### 继承
Django 的继承和 Python 的继承几乎一样，除了必须继承与 `django.db.models.Model` 之外。

三种继承的方式：
1. abstract base class: 希望父类持有一些信息（属性、方法等），让子类继承获得，并且父类不会单独使用。（比如定义一个通用的 `__repr__` 方法）
2. multi-table inheritance: 继承自已有的 model 并且子类父类都拥有自己的数据库表。
3. proxy models: 代理一个 model，不改变字段只修改行为。（比如添加一些新方法或者换掉 Manager）

#### 抽象基类
```python
from django.db import models

class CommonInfo(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```
只要添加 `abstract=True` 属性，就不会在数据库中建表。继承这个类的时候，meta也会自动继承但 `abstract=False`。meta也是可以继承的并且常常会这样处理：
```python
class Sub(CommonInfo):
    class Meta(CommonInfo.Meta):
        db_table = 'subclass'
```

#### 多表继承
多表继承是通过子类自动创建的 `OneToOneField` 来实现表关联的。先看一个例子
```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
```
尽管 Restaurant 实例也是具有 name 属性的。不同的是，在数据库层面， Restaurant 表并没有 name 这一列。

#### 委托
代理 model 和原 model 操作同一个数据库表，因此，QuerySet 返回原生的对象。但代理 model 可以在原基础之上增加自定义的操作，比如：更改 Manager，修改排序，添加新方法。
```python
class MyPlace(Place):
    objects = NewManager()  # 如果要替换默认管理器的话

    class Meta:
        proxy = True
        ordering = ['last_name']

    def do_sth(self):
        pass
```
如果只是想以抽象基类这样的风格，来添加一个manager相当于mixin而不是替换默认的。
```python
class ExtraManager(models.Model):
    ins = NewManager()

    class Meta:
        abstract = True


class MyPerson(Person, ExtraManager):
  class Meta:
      proxy = True
```

### Field 不许重写
值得一提的是，典型Python中，像这样的代码(子类同名属性覆盖父类属性)是很常见的：
```python
class A(object):
    name = 'a'
class B(A):
    name = 'b'
```
但在 Django 的 Field 里面是不允许的。

## Queries
> Django自带的一套CRUD的API, [full references](https://docs.djangoproject.com/en/1.10/ref/models/)包含更多的SQL子句。

### CRUD
- `Blog(name='Beatles Blog', tagline='All the latest Beatles news.')`  # INSERT
- `b5.name = 'New name'`  # 赋值操作 UPDATE
- `entry.blog = Blog.objects.get(name="Cheddar Talk")`  # UPDATE .. SET ForeignKey=...
- `b.save()`  # 上述操作只有在 save() 之后才会在数据库执行

> Retrive 是通过每个 model 对应的 Manager，默认的是 objects
> 使用它做查询会生成 QuerySet，它是 unique 和 lazy 的

- objects  #
    - `Class.objects.all()`
    - `Class.objects.filter(\*\*kwargs)`  # WHERE
    - `Class.objects.exclude(\*\*kwargs)`
    - `Entry.objects.filter(pub_date__year=2006)`  # 一个叫 lookup 的东西
    - `Entry.objects.get(pk=1)`  #　相当于对filter做切片[0]
    - 普通的 PYthon 切片也可以使用
    - `Entry.objects.filter(blog_id=4)`  # fk 通过 \_id 查询

> lookups 对应 WHERE，格式为 field__lookup=value
> 例如 Entry.objects.filter(pub_date__lte='2006-01-01')  # SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';

- lookups
    - `Entry.objects.get(headline__exact="Cat bites dog")`  # Entry.objects.get(headline="Cat bites dog") 实际执行的就是这个，SELECT ... WHERE headline = 'Cat bites dog';
    - `Blog.objects.get(name__iexact="beatles blog")`  # 大小写敏感
    - contains
    - startswith / endswith
    - pk

> SQL JOIN -- lookups

- `Entry.objects.filter(blog__name='Beatles Blog')`
- `Blog.objects.filter(entry__headline__contains='Lennon')`
- [多对多有点复杂](https://docs.djangoproject.com/en/1.10/topics/db/queries/#spanning-multi-valued-relationships)

> 对比同 instance 的不同 fields -- F()

- `>>> Entry.objects.filter(n_comments__gt=F('n_pingbacks'))`

> pk lookups

> 与 SQL LIKE 语义相对应的 lookups 可以很自然地使用

- `>>> Entry.objects.filter(headline__contains='%')`

> **建议使用赋值操作把 QuerySet 产生的缓存复用**
> [何时不会缓存](https://docs.djangoproject.com/en/1.10/topics/db/queries/#when-querysets-are-not-cached)

> Q 支持 SQL - AND & OR | NOT ~

```python3
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
```
相当于
```SQL
SELECT * from polls WHERE question LIKE 'Who%'
    AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
```

> 使用 `some_ins == another_ins` 会直接比较两个实例的主键值

> ins.delete()
> QuerySet.delete()  # 批量

> 复制：只需要 `pk = None`，如果有关联还要 `id = None`，不过关系不会被复制

> 更新多个对象 QuerySet.update(key=value)，但它只能对一个表改动

---

## Aggregation
> 汇总 -- 例如 MySQL 给出5个 aggregation function(AVG, COUNT, MAX, MIN, SUM)

```python3
"""Aggretion Example"""

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
```

- count  # 类似 len()
    - `Book.objects.count()`
    - `Book.objects.filter(publisher__name='mike').count()`
- Avg  #
    - `Book.objects.all().aggregate(Avg('price'))`
- Max  #
    - `Book.objects.all().aggregate(Max('price'))`

### 建立在 QuerySet 之上
> 对 QS 使用 aggregation function, 比如：求所有书本的均价
> 使用 aggregate() -- return dict

`Book.objects.all().aggregate(Avg('price'))` 等于 `Book.objects.aggregate(Avg('price'))`

```python3
>>> from django.db.models import Avg, Max, Min
>>> Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
{'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}
```

### 对 QS 里的每个 ins 使用 aggregation
> 比如：求每本书的作者数量
> 使用 annotate() -- 返回的不是一个 dict 而是 value

```python3
>>> from django.db.models import Count
>>> q = Book.objects.annotate(Count('authors'))
# 使用 annotate() 会为 QS 里的每个 ins 添加一个属性
>>> q[0].authors__count
2
# 也可以给属性命名
>>> q = Book.objects.annotate(num_authors=Count('authors'))
>>> q[0].num_authors
2
```

### 跨模型
```python3
>>> from django.db.models import Max, Min
# 每个书店最贵最便的书
>>> Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
# 所有书店最贵最便宜的书
>>> Store.objects.aggregate(min_price=Min('books__price'), max_price=Max('books__price'))
```

---

## TableSpaces
> [wikipedia关于表空间的介绍](https://en.wikipedia.org/wiki/Tablespace)
> 简单来说就是组织磁盘布局，用于优化数据库系统性能。
> 但也只有 PostgreSQL/Oracle 支持， SQLite/MySQL 均不支持。

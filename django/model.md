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


## Models

#### 字段选项
- null
- blank
> null是数据库的空值，blank是表单数据验证能否为空。
- choices
- default
- help_text
- primary_key
> 默认把自带的id作为pk
- unique

#### 关系
- many-to-one
> fk = django.db.models.ForeignKey(ForeignModel)

- many-to-many
> many = django.db.models.ManyToManyField(ManyModel)
> 多对多在关联的两个模型中的任一个添加多对多Field都可以

- one-to-one
> 当某个对象想扩展自另一个对象时，最常用的方式就是在这个对象的主键上添加一对一关系。

#### Meta
> 任何不是字段的数据


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

#### Django Overview
> 如何用 Django 写一个 database-driven 的 web app。

1. 设计 Model
 > 一个 model 就是一个数据库的 table

2. 创建 table
 > `python manage.py migrate`

3. models 的 api

4. 基于 model 的 admin
 > 一个经典的 workflow：设计好 models 后通过 admin 给员工、客户（Django 为这些 User 提供了验证机制）提供CRUD的功能。再去开发公开的页面。

5. 设计 URL
 > 正则匹配 url 到 views 的映射：把请求和 url 参数等等提供给 views

6. 编写 Views
 > 接收请求，处理参数，返回响应，调用 template 和渲染数据。

7. 编写 templates
 > 同样的子模板，继承不同的模板，是不同前端version的生产方式。

> 从 MVC 的设计模式来理解 Django

#### 第一个 Django App

##### Step one -- setup & request and response object

1. 在 web server 上，Django project 的代码不该放在 document root，建议放在 `/home/mycode` 中。（不像老 PHP 放在 `/var/www` 中）
2. `django-admin startproject projectname`
        mysite/                     # 可 rename
        	manage.py
            mysite/
            	__init__.py
                settings.py
                urls.py
3. *You should always use **include()** when you include other URL patterns. admin.site.urls is the only exception to this. 旧版的 Django 使用 `include(admin.site.urls)`*
4. `django.conf.urls.url()`
 > 1. re
 >  - 从上到下匹配 request 的 url
 >  - 忽略 GET / POST 参数，如：http://example.com/myapp/ 和 http://example.com/myapp/?page=3 都会匹配到 myapp/
 > 2. view
 >  - 匹配 re 的 request 会指向这个 view，传一个 HttpRequest 对象和 meta data
 > 3. 可选参数 kwargs
 > 4. 可选参数 name (view 的命名空间)

##### Step two -- DB and Model
1. Django settings `DATABASE` 字典的 `default` 有4个选项： `django.db.backends.whichdb`(sqlite3, postgresql, mysql, oracle)
> 除了 sqlite3 只需要设置 `ENGINE` 和 `NAME` 外，其他 DB 还要设置 `USER` `PASSWORD` `HOST` 等其他值，同时要创建相应的 database 让 Django 连接和建表。（`migrate` 会根据 `INSTALLED APPS` 列表为每一个 app 建表，每个 model 类一张表。）

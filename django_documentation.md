### 阅读 Django 文档

## 概览

### 组织形式
> 下面四个部分，从浅入深。尽量依次学习。

- Tutorials
- Topics
- References
- How-to

### Tutorials

- Overview
- How to build a simple web app
- Advanced

### Key Topics about Django
- 安装 Django
- Models & DB
- 处理 Http 请求
- Forms
- Templates
- Class-based Views
- Migrations
- 处理 files
- 测试
- 用户验证
- Conditional View Processing
- Cryptographic signing
- 邮件发送
- 国际化 / 本地化
- 日志
- 翻页
- Web 安全
- Performance & Optimization
- 序列化
- Settings
- Signal
- System check framework
- 拓展包

### API Reference

### How-to

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
	> 	- 从上到下匹配 request 的 url
	> 	- 忽略 GET / POST 参数，如：http://example.com/myapp/ 和 http://example.com/myapp/?page=3 都会匹配到 myapp/
	> 2. view
	> 	- 匹配 re 的 request 会指向这个 view，传一个 HttpRequest 对象和 meta data
	> 3. 可选参数 kwargs
	> 4. 可选参数 name (view 的命名空间)

##### Step two -- DB and Model
1. Django settings `DATABASE` 字典的 `default` 有4个选项： `django.db.backends.whichdb`(sqlite3, postgresql, mysql, oracle)
> 除了 sqlite3 只需要设置 `ENGINE` 和 `NAME` 外，其他 DB 还要设置 `USER` `PASSWORD` `HOST` 等其他值，同时要创建相应的 database 让 Django 连接和建表。（`migrate` 会根据 `INSTALLED APPS` 列表为每一个 app 建表，每个 model 类一张表。）
> **`python manage.py sqlmigrate` and `python manage.py check` also helps**

#### Step three -- views
> 常见的 blog view 设计：最近几条、entry、年、月、日、评论

1. Django 的 URLConf 看如下例子：
	```py
    #! polls/views.py
    def results(request, id):
    	return HttpResponse("You're looking at results of question %s" % id)
    #! polls/urls.py
    from . import views
    urlpatterns = [
    	url(r'^(?P<id>[0-9]+)/$)', views.results, name='results')
    ]
    ```
    - 当访问 /polls/34/results/ 时，会这样调用函数：`results(request=<HttpRequest object>, id='34')
    - `/` 会先看根目录
    - 请求首先会看 `project/urls.py` 的匹配模式，这样就可以通过 `include()` 为不同的 app 提供前缀。切割 `polls/`
    - `(?P<arg>pattern)` 会把匹配 re 的部分当作参数传递给 view function，参数名就是 <> 里的名字。切割 `34/`
    - 最后剩下 `results/`
2. view 的必须任务是：接收 http request，返回 http response（所谓“遵循同一通讯规范”）。
	> 上述是根本，在 Django 中提供了很多其他 options：*Your view can read records from a database, or not. It can use a template system such as Django’s – or a third-party Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.*
3. namespace：使用 `templates/appname/` 来构造模板结构。如果使用 `'APP_DIRS': True`，结构如
	 ```
     blog/
     	- templates/
     		- blog/
     			- index.html
     ```
但 djangoproject 使用了更为简洁的方式 `'DIRS': [os.path.join(BASE_DIR, 'project-package/templates')]`，同时，
	```
    project-package/
    	- templates/
    		- blog/
    			- index.html
    		- contact/
    			- index.html
    		- dashboard/
    			- index.html
    ```
4. view 渲染模板的函数
	```py
    -------
    from django.template import loader
    def index(request):
    	template = loader.get_template('polls/index.html')
    	context = {}
        return HttpResponse(template.render(context, request))
    -------
    from django.shortcuts import render
    def index(request):
    	context = {}
        return render(request, 'polls/index.html', context)
    -------
    from django.http import Http404
    def detail(request, id):
    	try:
        	q = Question.objects.get(pk=id)
            context = {'question': q}
        except Question.DoesNotExist:
        	raise Http404('not exist')
        return render(request, 'polls/detail.html', context)
    -------
    from django.shortcuts import get_object_or_404
    def detail(request, id):
    	# get 不到则 raise Http404
    	q = get_object_or_404(Question, pk=id)
        context = {'question': q}
        return render(request, 'polls/detail.html', context)
    ```
5. template 中的 namespace
	- `<a href="/polls/{{ question.id }}/">`
	- `<a href="{% url 'detail' question.id %}">`
	> 使用第二种模式，可以只改动 urls.py 里 `url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),` 的 re 来改变 url 映射。
	- 在 `polls/urls.py` 写入 `app_name = 'polls'`，给 app 提供命名空间 `<a href="{% url 'polls:detail' question.id %}">`，不同 app 就可以使用相同 view 函数名，只需要在 template 里指定 `app_name:func_name`。

##### Step four -- form
    - 如上所述的 namespace 模式 `polls:index`, 在 views 里面用 reverse
    可以解析出 `reverse('polls:results', args=(p.id)) -> '/polls/3/results/'`
    - modelview 在 urls.py 里面期待的是 `(?P<pk>)` pk

#### HttpRequest / HttpResponse

django.http 中:

class HttpRequest
属性:
- scheme: http / https
- body: bytes, 利于处理非HTML的数据.
- path: '/path/of/url/'
- path_info:
- content_type:
- content_params:

- method: 'GET' / 'POST' / 'PUT' ...
- encoding: writable
> GET / POST 在 Django 中都是类字典形式的
> 原始的 GET 字典是 url 中的 query: ?key=value&key=value
> 原始的 POST 字典是 body 中的: key=value&key=value
- GET:
- POST: 表单中的数据
- COOKIES:
- FILES: FILES 只有在请求的方法为POST且提交的<form>带有enctype="multipart/form-data" 的情况下才会包含数据.
- META: 包含所有的HTTP headers
- resolver_match:
方法:
- get_host():
- get_port():
- get_ful_path(): '/path/of/url/?print=true'
- build_absolute_uri(): "https://example.com/music/bands/the_beatles/?print=true"
- get_signed_cookie():
- is_secure(): True/False, 是否HTTPS
- is_ajax(): if HTTP_X_REQUESTED_WITH == 'XMLHttpRequest'
- read(size=None):
- readline():
- readlines():
- xreadlines():
- \__iter\_\_():

class HttpRespons
属性:
- content: bytes
- charset:
- status_conde:
- reason_phrase:
- streaming:
- closed:
方法:
- __init__(content='', content_type=None, status=200, reason=None, charset=None)
- has_header():
子类:
- JsonResponse
- StreamingHttpResponse
    - 传入迭代器
- FileResponse

# User Authentication in Django
> 默认用户系统包括：帐号、组、权限、cookie/session、可配制的密码hash、用户表单和视图

## 启用
```py
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
```

## User 对象
`django.contrib.auth.models.User`

### 基本属性
- username
- first_name
- last_name
- email
- password

### create
`User.objects.create_user(username, email=None, password=None, **extra_fields)`

### createsuperuser
### changepassword
`python manage.py changepassword <username>`

`user_ins.set_password(raw_password)`

### authenticate
`authenticate(request=None, **credentials)`

```py
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
if user is not None:
    ...
```
一般情况下用不着这个底层的认证函数，更多时候使用自带的用户系统只需要`@login_required`

## 权限/授权

## Web 请求中的认证

### login
```py
from django.contrib.auth import authenticate, login
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
```
必须先调用`authenticate()`，如果直接从数据库查询得出一个user来login，会失败

### logout
```py
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
```

### login_required
原始方法
```py
from django.conf import settings
from django.shortcuts import redirect
def my_view(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
```
装饰器
```py
from django.contrib.auth.decorators import login_required
@login_required
def my_view(request):
    ...
```
系统自带的 login 视图
```py
from django.contrib.auth import views as auth_views
url(r'^accounts/login/$', auth_views.LoginView.as_view()),
```
自定义 login 视图
```py
@login_required(login_url='/accounts/login/')
url(r'^accounts/login/$', accounts.views.login),
```

## 默认的认证视图们
> 只有视图，使用默认的 form ，并且没有模板，需要自己写模板，也可以自定义 Forms

### 直接使用

```py
urlpatterns = [
    url('^', include('django.contrib.auth.urls'))
]
```

就能得到一下路由和视图
```py
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
```

也可以单独引用某个视图
```py
from django.contrib.auth import views as auth_views
urlpatterns = [
    url('^change-password/$', auth_views.PasswordChangeView.as_view()),
]
urlpatterns = [
    url('^change-password/$', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
]
```

### 视图们的介绍

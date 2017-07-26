# images, JavaScript, CSS...
> INSTALL_APPS里的 dango.contrib.staticfiles 是管理静态文件的工具.

1.
```py
STATIC_URL = '/static/'  # 静态文件的url前缀
```

2.
```html
{% load static %}
<img src="{% static 'my_app/example.jpg' %}"/>
<img src="/static/my_app/example.jpg"/>
```

3.
默认是在每个APP里组织静态文件目录的, 于是乎, 是从 app/static/app/ 那里寻找static


或者可以添加额外的寻找路径
```py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # path1
    '/var/www/static/',  # path2
]
```

4. 上述步骤3, 在开发阶段, 只要 DEBUG=True 就能生效. 因为 django.contrib.staticfiles 的存在.

5. (plan B)除非你没事找事地删掉 django.contrib.statifiles, 否则不需要这一步. 手动地让 Django 服务器来实现 url '/static/' 和静态文件目录的映射.
```py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

6. 但是5中的 helper function 在开发阶段支持文件上传有点用处
```py
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

7. 上诉4-6在到部署阶段都会被真正的服务器替代, collectstatic 命令会把所有开发阶段寻找 static 的目录复制到 STATIC_ROOT 一个目录底下. 大致的流程举个例子:
```
比如模板中的一个css引用
<link rel="stylesheet" href="static/css/dashboard.css">

Nginx中会直接分发这个请求
location /static {
    alias /home/mac/sites/www.todolist.com/static;
}
```

> 另外值得一提的是： MEDIA 是不同的一样东西
> static 的出现是为了处理（js/css/images...）等静态文件
> media 则处理 Django 的文件上传（FileField/ImageField...）
> 与之相关的两个属性书写格式为： `MEDIA_URL='/media/'` 和 `MEDIA_ROOT=os.path.join(BASE_DIR, 'media')`

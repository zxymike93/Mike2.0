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
- \_\_iter\_\_():

class HttpRespons
属性:

- content: bytes
- charset:
- status_conde:
- reason_phrase:
- streaming:
- closed:
  方法:
- \_\_init\_\_(content='', content_type=None, status=200, reason=None, charset=None)
- has_header():
  子类:
- JsonResponse
- StreamingHttpResponse
  - 传入迭代器
- FileResponse

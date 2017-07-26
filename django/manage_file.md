# Managing files

Django 默认使用 `MEDIA_ROOT / MEDIA_URL` 两个 settings 来设置文件系统的存储位置和url前缀。

## Using files in models

使用 `FileField / ImageField` 都能得到 Django 提供的一套文件 API([File's methods](https://docs.djangoproject.com/en/1.11/ref/files/file/#django.core.files.File))

```python3
from django.db import models
class Car(models.Model):
    photo = models.ImageField(upload_to='cars')
```

## The File object
> Django 文件对象来自 `django.core.files.File` 类

实例化一个 File 实例
```python
from django.core.files import File
with open('/path/to/file', 'w') as f:
    myfile = File(f)
    myfile.write('dududu')
```

## File Storage
> `DEFAULT_FILE_STORAGE` settings属性决定存储系统
> 默认 `DEFAULT_FILE_STORAGE='django.core.files.storage.FileSystemStorage'`

### Storage objects

```python
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

f = ContentFile('hello world')
path = default_storage.save('/path/to/store/file', f)
```
[API](https://docs.djangoproject.com/en/1.11/ref/files/storage/)

### 内置文件存储类

通过 `FileSystemStorage` 类可以自定义存储方式
使用第一个例子的 Car 类

```python
[...]
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/i/like/to/store/here')
[...]
    photo = models.ImageField(storage=fs)
```

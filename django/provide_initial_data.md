两种方式：
- fixtures
- migrations


## fixtures

记住两条命令：
- python manage.py dumpdata
- python manage.py loaddata

路径：
- 每个 app 的 fixtures 子目录下
- settings 的 FIXTURE\_DIRS 属性


## migrations

自动运行初始化数据库的方式：
- RunPython
- RunSQL

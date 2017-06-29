# Nginx 文档

## Beginner's Guide
> How-to: start / stop / reload (config)
> 配置文件结构, 包括如何: 支持静态文件 / 代理 / 连接FastCGI应用

> Nginx 有一个主进程和N个子进程:
> 主进程负责读取/评估config和控制子进程
> Nginx基于event-based model分发请求到子进程中
> 一般配置文件中定义子进程数

> 配置文件默认为 nginx.conf
> /usr/local/nginx/conf
> /etc/nginx
> /usr/local/etc/nginx

### start / stop / reload
```nginx -s <command>```

- stop

- quit
> 等待所有请求完成后关闭

- reload 
> 检查语法, 成功: 开启新进程, 停止旧进程. 失败: 回滚到旧进程

- reopen

**kill -s QUIT <nginx.pid>(in /var/run or /usr/local/nginx/logs)**
**ps -ax | grep nginx**
**/var/log/nginx or /usr/local/nginx/logs 中的 access.log/error.log**

### 配置文件

```
main {
    events {
    }
    http {
        server {
            location {}
        }
    }
}
```

#### 服务静态文件
例如: /data/www (html文件) /data/images (图片)
```
location / {
    root /data/www;
}
location /images/ {
    root /data;
}
```
www.example.com/index.html -> /data/www/index.html
www.example.com/another/index.html -> /data/www/another/index.html
www.example.com/images/1.gif -> /data/images/1.gif
Nginx会使用匹配到的前缀最长的location块

#### 代理服务器
```
server {
    listen 8080;
    root /data/up1;  # 没单独root的location使用这个root

    location / {
        proxy_pass http://localhost:8080/;
    }
    location ~ \.(gif|jpg|png)$ {
        root /data/images;
    }
}
```
正则匹配更优先

> 从CSAPP网络部分了解到，现代机器之间实现相互通信，使用 **client - server** 模型。
>> *插一句：无论是 client／server 中的任一者，都只是建立在计算机架构的网络原型上的抽象概念。
具体一台计算机，从到物理角度是 I/O设备，从软件角度是 计算机系统的网络接口。
一台实际的物理机可以有N个网络相关的应用，每个应用还存在N个进程。
（这么说并不准确和严谨，不过能剥离 client-server模型 和 计算机及其系统 两者之间的概念。）*

> 另外涉及的一个概念就是：协议——在这个模型之中就是不同端之间通信都遵循的规范。就像写信要有写信的规范。
>> HTTP 是应用层次里最广（总之就是web开发必须掌握的）协议，当然，按照 OSI层级，还有 TCP/IP 这样重要的协议。

本文的目的，就是要对 HTTP协议 作最基本够用的总结。

## 目录
1. Web Simply Foundation
2. HTTP Overview
3. Request and Response
4. Status Code
5. Web Server
6. HTTP Headers
7. HTTPS
8. Authentication
9. Protocol Beyond HTTP
10. HTML and Web App
11. Web Exploit


## 1. 网络基础
> 分别从协议、Python两个角度来理解网络通信。

先看下面4个程序，它们要完成同样的一件事：向googlemaps的API发出请求，得到响应中的部分数据。

1. 这是3rd-party的库，针对googlemap的geocode API处理。
    - 输入地址名
    - 从预定义的数据结构中（这里是类）读取数据
```python
from pygeocoder import Geocoder

def geocode(addr):
    print(Geocoder.geocode(addr)[0].coordinates)
```

2. 这是著名的3rd-party库requests。
    - 把地址构建成完整的url
    - 指定请求方法
    - 把响应构建成指定的格式
    - 读取
```python
import requests

def geocode(addr):
    params = {
        'address': addr,
        'sensor': 'false',
    }
    url = 'http://maps.googleapis.com/maps/api/geocode/json'
    r = requests.get(url, params=params).json()
    print(r['results'][0]['geometry']['location'])
```

3. Python内置模块的 http.client / urllib.parse / json
    - 构建完整的url
    - 建立连接和指定请求方法
    - 把响应构建成指定的格式
    - 读取
```python
import json
from http import client
from urllib.parse import quote_plus

def geocode(addr):
    path = '/maps/api/geocode/json'
    url = '{}?address={}&sensor=false'.format(path, quote_plus(addr))
    conn = client.HTTPConnection('maps.google.com')
    conn.request('GET', url)
    r = conn.getresponse().read()
    resp = json.loads(r.decode('utf-8'))
    print(resp['results'][0]['geometry']['location'])
```

4. Python 内置的 socket
    - 构建完整的 HTTP 报文
        - 请求行（方法 url 协议版本）
        - 请求头部
    - 编码，发送请求
    - 得到响应，编码
    - 构建json格式
```python
import socket
from urllib.parse import quote_plus

def geocode(addr):
    s = socket.socket()
    s.connect(('maps.google.com', 80))
    method = 'GET'
    path = '/maps/api/geocode/json'
    params = '?address={}&sensor=false'.format(quote_plus(addr))
    protocol = 'HTTP/1.1'
    headers = {
        'Host': 'maps.google.com:80',
        'User-Agent': 'search4.py (Foundations of Python Network Programming)',
        'Connection': 'close',
    }
    header_str = ''
    for k, v in headers.items():
        header_str += '{}: {}\r\n'.format(k, v)

    request = '{} {}{} {}\r\n{}\r\n'.format(
        method, path, params, protocol, header_str)
    s.sendall(request.encode('ascii'))

    response = b''
    while True:
        r = s.recv(4096)
        if not r:
            break
        response += r
    print(r.decode('utf-8'))
```

从下往上，可以理解为一个封装的过程。
    - socket模块在绝大部分情况下，是Python程序员会遇到的最底层的网络编程库了。再往下就是 TCP/IP 协议。
    - 为了封装 HTTP 协议，解决 url 编码问题，各种文本数据格式、编码，Python 有对应的 http ／ urllib ／ json 等库和 bytes 编码。
    - requests 提供上面这一些常见实现的封装，用更简单易读的方式提供 API
    - 有时候我们使用外部网络工具（比如一些网站的 API），还有特地为其编写的第三方库能更简单地编写代码。

通过 Python，我们简单地了解到协议：只不过是一些（使用编码的）字符或文本，通过约定的格式书写。
其中 HTTP协议 的工作机制大致如上面所述，只是程序员大部分时间都在 1 2 层工作（类似于用 Django 处理，或者用 DRF 为 Django 的特定事务再封装一层）。
[在接下来我会花时间分析 Django 源码中这些处理 HTTP协议 相关的部分，如：URL / request&response]()
但在具体了解协议细节和编程实现之前，了解 HTTP 之下的 TCP/IP 协议，能更好地理解网络的工作，理解这个“黑箱”。

###

TCP/IP协议 中最重要的概念是分层，下图是简化的 TCP/IP通信传输流：
[](https://etianqq.gitbooks.io/http/content/TCP-IP%20model2.jpg)

在这个简单的模型里，各协议对应的层次：
- 应用层：HTTP
- 传输层：TCP
- 网络层：IP
- 链路层：网络相关的硬件以及驱动等

以这个模型为基础的一次通信，是先从上往下地进入到互联网中，到达目的设备，再从下网上得重新构成完整HTTP报文的。
再具体一点地描述，假设浏览器访问 google.com 这些关键部分的工作，如下：
    请求：
    1. 域名被 DNS 解析为 IP地址
    2. 浏览器（客户端）负责构造一个完整的 HTTP报文
    3. TCP 把报文分割为若干部分，
    4. IP 把目的地的 IP地址和MAC地址 附上
    5. 经过多个 routing，每个 routing 根据下一个 routing 的MAC地址进行转发
    6. 包的一方，通过 TCP协议 重组原来的报文
    7. 最后再由 HTTP协议 解读这段信息

ip：routing 处理到下一站的传输
tcp：可靠性、完整性
dns：域名和ip间的转换



## 7. HTTPS
TCP/IP 是公开通信的协议，而 HTTP 也是明文传输的。为了安全，只要使用了 SSL/TLS 通信的 HTTP（准确来说是 HTTP 先经过 SSL 再和 TCP 通信），称之为 HTTPS。（另外还有对 HTTP 报文主体加密的方式）

> Q: What are the differences between HTTP and HTTPS?

加密 + 证书 + 完整性保护

> 加密 ( SSL 中使用的技术叫公开密钥，简称密钥。和“公钥”不是一个概念。)

对称加密： c / s 任一方，有一把共享密钥，在 HTTP 传输数据的时候把密钥带上。两者一个同一个密钥加密解密。

非对称加密：比如 client 有一对公钥+私钥，请求时把公钥附上。server 响应的内容用公钥来加密，client 再把接受到的内容用私钥解密。

HTTPS 是采用混合机制的：一般的通信使用共享密钥的方式，但首次共享密钥的方式，是通过非对称加密安全传输的。

> 证书

就是第三方机构对公开密钥加上数字签名证书，server 把这样的公开密钥发送给 client 后，client 通过从机构事先得到的验证方式解密验证这个密钥是不是正经的网站发来的。

> 完整性

HTTP 本身也常用 MD5，SHA-1 这种散列算法来验证完整性的，不过 HTTPS 用更复杂的机制。

**最后，HTTPS 因为需要再处理一层 SSL 以及更吃网络资源，只有在需要安全通信的场景下会使用。不过随着这方面的技术提高，使用 HTTPS 也成为一种趋势，特别是企业级的网站。所以值得了解和关注。**

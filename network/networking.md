### TCP基础
> N个应用程序共享一条连接互联网的线路. TCP把每个通信拆分为很小的信息包, 因此用户感觉是几个程序同时在通信.

#### 寻址
> IP为目的地, 每台机器都有唯一的IP. 端号是这台机器上每个程序的唯一标识.

#### 保证数据的完整性
> 每个信息包都有验证码, TCP要求接收方收到每个包都反馈一下, 以此确认对方是否收到完整的信息.
> 包里面还有序列号, 接收方收到很多打散的包后, 会按序列号组织包顺序.

#### 路由
> 信息从一台机器到另一台机器要经过Internet上的很多地方, 路由器是传输这些包的机器.

#### 安全
> SSL和TLS

### Server/Client模式
> 服务器一直监听, 客户端总是开始申请连接的.

#### 端口
> web server默认80. 实际上在 /etc/services 里可以看到官方分配的列表.
> 一般而言程序端口开在 1024-65535 间.
> 客户端的端口一般由操作系统随机分发, server按照client请求时的端口返回信息即可.

### UDP
> 它只保证收到的数据是完整的: 不保证数据能否被收到, 是不是只接收一次,
> 顺序是否一致. 但它非常快.

### 物理和ethen
> TCP/IP协议可以在不同物理网络硬件之间传输信息.
> 以太网的一个最主要特点: 可以向本地网络所有工作站广播信息包.
> 我一般提到的内网通信, 就是以太网通信: 通过比较IP的头几位, 确定通信方是否在同一以太网内, 否则, 就需要先发到本地路由器上再传送到Internet上.

### socket
> 网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket。它是跨平台的。
> Python Lib/socket.py 实现了 socket 的 Python 接口。
- socket.socket()
- socket.recv(buff)
- socket.connect((host, port))
- socket.send(bytes)
- socket.sendall(bytes)
- socket.bind((host, port))
- socket.listen(int)
- socket.accept() -> (conn, addr) -> addr=host,port

### socket

### urllib
- urllib.request.urlopen()

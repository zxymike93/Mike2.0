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

## 7. HTTPS

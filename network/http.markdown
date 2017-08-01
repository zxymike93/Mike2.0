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

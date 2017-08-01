import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = socket.getservbyname('http', 'tcp')
print('http/tcp use port', port)
s.connect(('www.baidu.com', port))
print('client', s.getsockname())
print('server', s.getpeername())

import socket


host = ''
port = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 把 socket 设置为 reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定一个 host:port 作为程序的地址
s.bind((host, port))
# enable a server to accept connections
s.listen(1)

print('Listening on port {}'.format(port))

while True:
    # socket.accept() 返回 client socket 对象和地址
    connection, addr = s.accept()
    print(addr)
    with connection.makefile('rwb', 0) as f:
        f.write('Welcome {}\nYou can write something'.format(addr).encode())
        line = f.readline().strip()
        f.write('You enter {} chars'.format(len(line)).encode())
    connection.close()

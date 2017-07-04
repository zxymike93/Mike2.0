import socket


host = ''
port = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print('Listening on port {}'.format(port))

while True:
    connection, addr = s.accept()
    with connection.makefile('rwb', 0) as f:
        f.write('Welcome {}\nYou can write something'.format(addr).encode())
        line = f.readline().strip()
        f.write('You enter {} chars'.format(len(line)).encode())
    connection.close()

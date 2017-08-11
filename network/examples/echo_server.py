import socket


server = socket.socket()
server.bind('localhost', 10000)
server.listen(5)


while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    if data:
        conn.sendall(data)
    else:
        break

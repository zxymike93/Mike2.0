import socket
import sys


port = 70
host = sys.argv[1]
filename = sys.argv[2]


# 创建一个 socket 对象
# socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接一个 remote server
# s.connect((host, port))

try:
    # 设置连接超时限制
    s.settimeout(10)
    s.connect((host, port))
except socket.gaierror as e:
    print(e)
    sys.exit(1)
except socket.timeout as e:
    print(e)
    sys.exit(1)

# socket.send(bytes) 返回发送了多少 bytes
# 一般会用循环来实现完全发送数据
# socket.sendall(bytes) 则持续地发送, return None if success
s.sendall('{}\r\n'.format(filename).encode())

while True:
    # socket.recv(buff_size)
    buf = s.recv(2048)
    if not buf:
        break
    sys.stdout.write(buf.decode())

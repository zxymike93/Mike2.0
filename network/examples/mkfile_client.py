import socket
import sys


port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# 几乎和 open() 一样
# socket.makefile(mode='r', buffering=None, *, encoding=None, errors=None, newline=None)
with s.makefile('rwb', 0) as f:
    f.write('{}\r\n'.format(filename).encode())
    for line in f.readlines():
        sys.stdout.write(line.decode())

# 关闭 socket 的 file-objects 不会关闭 socket 对象
s.close()

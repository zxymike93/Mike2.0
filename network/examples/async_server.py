"""
POLLIN: there is data to read
POLLPRI: urgent data to read
POLLOUT: Ready for output: writing will not block
POLLERR: Error condition of some sort
POLLHUP: Hung up
POLLRDHUP: Stream socket peer closed connection, or shut down writing half of connection
POLLNVAL: Invalid request: descriptor not open
"""

import select

from zen_utils import create_socket, parse_command, get_answer


def all_events_forever(poll_obj):
    """
    这个 loop 用来保存每一个 pollobj 的状态（fd 和 event 信号）
    因为每一轮 for 循环中都等于 next(obj) 然后返回 fd, event
    """
    while True:
        for fd, event in poll_obj.poll():
            yield fd, event  #


def serve(listener):
    # 一个 file: socket 字典
    sockets = {
        listener.fileno(): listener
    }
    addrs = {}
    receive = {}
    send = {}

    # select.poll() 生成一个文件描述符（可以理解为文件对象）
    poll_obj = select.poll()
    # register() 之后才可以 poll()
    poll_obj.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_obj):
        s = sockets[fd]
        # 挂起或error或invalid
        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            addr = addrs.pop(s)
            rb = receive.pop(s, b'')
            sb = send.pop(s, b'')
            if rb:
                print('Client {} sent {} then closed.'.format(addr, rb))
            elif sb:
                print('Client {} closed before sending {}.'.format(addr, sb))
            else:
                print('Client {} closed normally.'.format(addr))
            poll_obj.unregister(fd)
            del sockets[fd]
        # 监听的 socket 永远只是用来把收到的请求 socket 注册到 polling
        elif s is listener:
            conn, addr = s.accept()
            print('Connection from:', addr)
            conn.setblocking(False)
            sockets[conn] = addr
            # 把和客户端的 conn socket 注册到轮询中
            poll_obj.register(conn, select.POLLIN)
        # 如果有可读数据，每次轮询读4kb，然后存储到 receive 字典中
        # { socket: 已读数据 }
        # 读到 `?` 结束，存储到 send 字典
        # { socket: 所有数据 }
        elif event & select.POLLIN:
            more_data = s.recv(4096)
            if not more_data:
                s.close()
                continue
            # 返回 receive 字典中 key 的 value 或者 b''
            data = receive.pop(s, b'') + more_data
            if data.endswith(b'?'):
                send[s] = get_answer(data)
            else:
                receive[s] = data
        # 每个轮询都发送信息并切片 send 字典中 socket: data 的 data 长度
        # 因为 socket.send() 不一定一次把数据传完，但这样不会阻塞
        elif event & select.POLLOUT:
            data = send.pop(s)
            n = s.send(data)
            if n < len(data):
                send[s] = data[n:]
            else:
                poll_obj.modify(s, select.POLLIN)


if __name__ == '__main__':
    addr = parse_command('async server')
    listener = create_socket(addr)
    serve(listener)

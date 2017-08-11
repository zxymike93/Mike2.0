import select
import socket
import queue


server = socket.socket()
# not blocking
server.setblocking(0)
server.bind('localhost', 10000)
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}


while inputs:
    # select(i, o, [i, o]) 接受三个参数，incoming data to be read, outgoing
    # data in buffer, those may have error
    # 返回三个列表，相当于把参数中 input 写进缓存
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        # 服务端
        if s is server:
            conn, addr = s.accept()
            conn.setblocking(0)
            inputs.append(conn)
            message_queues[conn] = queue.Queue()
        #
        else:
            data = s.recv(1024)
            if data:
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]
    for s in writable:
        try:
            msg = message_queues[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.send(msg)
    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queue[s]

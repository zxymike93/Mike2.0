import asyncio

from zen_utils import get_answer, parse_command


class ZenServer(asyncio.Protocol):

    def connection_made(self, transport):
        """transport 是建立连接的那个 socket"""
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Connection from:', self.address)

    def data_received(self, data):
        self.data += data
        if self.data.endswith(b'?'):
            answer = get_answer(self.data)
            self.transport.write(answer)
            self.data = b''

    def connection_lost(self, exception):
        if exception:
            print('Client {} err: {}'.format(self.address, exception))
        elif self.data:
            print('Client {} sent {} then closed'
                  .format(self.address, self.data))
        else:
            print('Client {} closed'.format(self.address))


if __name__ == '__main__':
    addr = parse_command('asyncio using callbacks')
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ZenServer, *addr)
    server = loop.run_until_complete(coro)
    print('Listening at {}', addr)
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()

from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

from zen_utils import handle_conversation, parse_command


class ZenHandler(BaseRequestHandler):

    def handle(self):
        handle_conversation(self.request, self.client_address)


class ZenServer(ThreadingMixIn, TCPServer):

    allow_reuse_address = 1


if __name__ == '__main__':
    addr = parse_command('SocketServer')
    server = ZenServer(addr, ZenHandler)
    server.serve_forever()

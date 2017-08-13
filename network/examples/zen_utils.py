import argparse
import socket
import time


faq = {
    b'Beautiful is better than?': b'Ugly',
    b'Explicit is better than?': b'Implicit',
    b'Simple is better than?': b'Complex',
}


def get_answer(faq):
    time.sleep(0)
    return faq.get(faq, b'Error: unknown question.')


def parse_command(cmd):
    parser = argparse.ArgumentParser(description=cmd)
    parser.add_argument('host')
    parser.add_argument('-p', metavar='port', type=int, default=1060)
    args = parser.parse_args()
    addr = (args.host, args.p)
    return addr


def create_socket(addr):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(64)
    return s


def run_server(server):
    while True:
        conn, addr = server.accept()
        print('Connection from:', addr)
        handle_conversation(conn, addr)


def recv_until(conn, suffix):
    msg = conn.recv(4096)
    if not msg:
        raise EOFError('connection close.')
    while not msg.endswith(suffix):
        data = conn.recv(4096)
        if not data:
            raise IOError('received {!r} then connection close.'.format(msg))
        msg += data
    return msg


def handle_request(conn):
    faq = recv_until(conn, b'?')
    answer = get_answer(faq)
    conn.sendall(answer)


def handle_conversation(conn, addr):
    try:
        while True:
            handle_request(conn)
    except EOFError as e:
        print('Client socket {} has closed'.format(addr))
    except Exception as e:
        print('Error', e)
    finally:
        conn.close()

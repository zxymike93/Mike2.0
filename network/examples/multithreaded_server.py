from threading import Thread

import zen_utils


def start_threads(listener, workers=4):
    for i in range(workers):
        t = Thread(target=zen_utils.run_server, args=(listener,))
        t.start()


if __name__ == '__main__':
    addr = zen_utils.parse_command('Multithreaded Server')
    listener = zen_utils.create_socket(addr)
    start_threads(listener)

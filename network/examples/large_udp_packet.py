import argparse
import socket
import IN


if not hasattr(IN, 'IP_MTU'):
    raise RuntimeError('在你的操作系统和Python版本组合中，'
                       '找不到MTU(最大传输单元)')


def send_big_datagram(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
    s.connect((host, port))
    try:
        s.send(b'#' * 65000)
    except socket.error:
        mtu = s.getsockopt(socket.IPPROTO_IP, IN.IP_MTU)
        print('MTU:', mtu)
    else:
        print('Sent.')


if __name__ == '__main__':
    send_big_datagram('127.0.0.1', 1060)

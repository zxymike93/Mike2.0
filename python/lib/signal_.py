# 通过信号通知的形式实现异步事件
# 可以在进程间通信

import os
import signal
import time
import threading


# # 这个程序的进程是 57415
# # 注册 signal.signal 之后，立即回调（异步）
# # 进程继续往下执行 time.sleep
# # $kill -USR1 57415
# # $kill -USR2 57415
# # 发出信号(kill)，会执行 receive_signal 的 print （signal handler return)
# # 再继续本进程的 while 循环
#
# def receive_signal(signum, stack):
#     print('Receive: {}'.format(signum))
#     print('Stack: {}'.format(stack))
# 
# signal.signal(signal.SIGUSR1, receive_signal)
# signal.signal(signal.SIGUSR2, receive_signal)
#
# # SIGALRM 是其中一种特殊的信号
# # 系统会在指定时间向本进程发送信号
# # 常用于防止阻塞
#
# signal.signal(signal.SIGALRM, receive_signal)
# signal.alarm(2)
# print('This Python program\'s PID: {}'.format(os.getpid()))
# while True:
#     print('waiting..')
#     time.sleep(3)


# # 查询已注册的handler

# def alarm_received(n, stack):
#     return
# 
# signal.signal(signal.SIGALRM, alarm_received)
# # {<Signals.SIGABRT: 6>: 'SIGIOT', <Signals.SIGALRM: 14>: 'SIGALRM',
# # <Signals.SIGBUS: 10>: 'SIGBUS'}
# signals_to_names = {
#     getattr(signal, signum): signum
#     for signum in dir(signal)
#     if signum.startswith('SIG') and '_' not in signum
# }
# for value, signum in sorted(signals_to_names.items()):
#     # 查看哪个 handler 注册了哪个 signal
#     # signal.signal(signal.SIGALRM, alarm_received)
#     handler = signal.getsignal(value)
#     if handler is signal.SIG_DFL:
#         handler = 'SIG_DFL'
#     elif handler is signal.SIG_IGN:
#         handler = 'SIG_IGN'
#     print('{:<10} ({:2d})'.format(signum, value), handler)

# # 忽略
# # Ctrl+C 发出的 keyboardinterrupt 信号(或者 `kill -INT $pid`)
# # 会被忽略
# # 只有直接杀死整个进程或者杀死 USR1 才会有效
#
# def do_exit(sig, stack):
#     raise SystemExit('退出')
# 
# signal.signal(signal.SIGINT, signal.SIG_IGN)
# signal.signal(signal.SIGUSR1, do_exit)
# print('process id: {}'.format(os.getpid()))
# signal.pause()

# # 信号在线程间的传送一般不太管用
# # 因为Python的实现方式决定signal只能由主线程收到
# # 下面在本程序主线程中分别创建 receiver / sender 线程
# # 尽管 receiver 线程执行 signal.pause 等待信号
# # 结果 sender 发送的 kill 信号仍然由 mainThread 收到
# 
# def handler(num, stack):
#     print('线程 {1} 收到信号 {0}'.format(
#         num, threading.currentThread().name))
# 
# signal.signal(signal.SIGUSR1, handler)
# 
# def wait_for_signal():
#     print('线程 {} 等待信号'.format(
#         threading.currentThread().name))
#     signal.pause()
#     print('结束等待')
# 
# receiver = threading.Thread(target=wait_for_signal, name='receiver')
# receiver.start()
# time.sleep(1)
# 
# def send_signal():
#     print('线程 {} 发送信号'.format(
#         threading.currentThread().name))
#     os.kill(os.getpid(), signal.SIGUSR1)
# 
# sender = threading.Thread(target=send_signal, name='sender')
# sender.start()
# sender.join()
# 
# # join 会 block 直到线程 terminate
# # 先发出 alarm 信号避免 receiver 收不到信号阻塞
# signal.alarm(2)
# receiver.join()

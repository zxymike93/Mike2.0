from ctypes import cdll

mydll = cdll.LoadLibrary('hello.so')
mydll.hello()

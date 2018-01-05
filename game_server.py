import socket
import sys


HOST = ''
PORT = 8888


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print 'Bind failed %s' % msg
	sys.exit()

print 'socket bind complete'

print 'waiting for message...'
while True:
	data,address = s.recvfrom(1024)
	print data, address
	s.sendto('this is UDP Server', address)

conn.close()
s.close()

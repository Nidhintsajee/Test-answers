from socket import *

LOCAL_ADDR = ('127.0.0.1', 8000)

fd = socket(AF_INET, SOCK_DGRAM)

fd.bind(LOCAL_ADDR)

while True:

	dat,addr=fd.recvfrom(1000)

	print 'Client:'+dat

	msg=raw_input('Server:')

	fd.sendto(msg,addr)

s.close()

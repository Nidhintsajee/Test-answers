from socket import *

TO_ADDR = ('127.0.0.1', 8000)

fd = socket(AF_INET, SOCK_DGRAM)

while True:
	
	msg=raw_input('CLient:')

	fd.sendto(msg,TO_ADDR)
		
	dat,addr=fd.recvfrom(1000)

	print 'Server:'+dat


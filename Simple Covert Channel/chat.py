import sys
import socket
from time import time
from binascii import unhexlify

ZERO = 0.025
ONE = 0.1
port = 1337
ip = "192.168.2.8"
covert_bin=""

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    data = s.recv(4096)
    while (data.rstrip("\n") != "EOF"):
    	sys.stdout.write(data)
    	sys.stdout.flush()
    	#data = s.recv(4096)
    
        t0=time()
        data = s.recv(4096)
        t1=time()
        delta = round(t1-t0,3)
        if (delta >= ONE):
        	covert_bin+="1"
        else:
        	covert_bin+="0"
    s.close()
except Exception as e:
    print e

covert = ""
i=0
while(i<len(covert_bin)):
	b = covert_bin[i:i + 8]
	n = int("0b{}".format(b), 2)
	try:
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	i+=8


print covert

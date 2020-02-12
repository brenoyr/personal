import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 1337
s.bind(("", port))

s.listen(0)

c, addr = s.accept()

import time
from binascii import hexlify

covert = "secret" + "EOF"
covert_bin = ""
for i in covert:
	covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

ZERO = 0.025
ONE = 0.1

msg = "Some message..."
n = 0
for i in msg:
	c.send(i)
	if(covert_bin[n] == "0"):
		time.sleep(ZERO)
	else:
		time.sleep(ONE)
	n = (n+1) % len(covert_bin)
c.send("EOF")
c.close()




# IPAddr: 192.168.1.6

from socket import *
import sys

# create client socket
client_socket = socket(AF_INET, SOCK_STREAM)

# variables for arguments from command line
server_ip = sys.argv[1]
server_port = sys.argv[2]
server_request = sys.argv[3]

# connect to server socket
client_socket.connect((server_ip, int(server_port)))

print "HTTP request to server:\nGET /{} HTTP/1.1\nHost: {}".format(server_request, server_ip)

# send the requested object
client_socket.send(sys.argv[3].encode())

# receive message from server
response = client_socket.recv(2048)
print "HTTP response from server:"
print response.decode()
print response

# close client socket
client_socket.close()

#########################################################
#   Name:       Breno Yamada Riquieri                   #
#   Class:      CSC450 - Computer Networks              #
#   Asgmt:      #3 - UDP                                #
#   Due Date:   10/14/2020                              #
#   Comments:   Python 2.7.17                           #
#               Ubuntu 18.04.5 LTS                      #
#########################################################
# My IPAddr during development: 192.168.1.6

from socket import *
import random
import time

# get IP address
hostname = gethostname()    
IPAddr = gethostbyname(hostname)

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('', 12000))
print "Server is ready to receive messages..."

while(True):
    message, client_address = server_socket.recvfrom(2048)
    message = message.decode()

    if random.randint(0,100) < 80:
        server_socket.sendto(message.encode(), client_address)
    else:
        time.sleep(1)

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

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('', 12000))
print "Server is ready to receive messages..."

while(True):
    message, client_address = server_socket.recvfrom(2048)
    message = message.decode()
    print "Received message: {}.\nFrom client: {}".format(message.decode(), client_address)


    modified_message = message.upper()
    print "Modified message: {}".format(modified_message.decode())

    server_socket.sendto(modified_message.encode(), client_address)
    print "\nMessage sent\n"
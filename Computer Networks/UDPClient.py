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

client_socket = socket(AF_INET, SOCK_DGRAM)

server_ip = sys.argv[1]         # 192.168.1.6 during development
server_port = sys.argv[2]       # 12000
server_pings_no = sys.argv[3]

print "Pinging {}:".format(server_ip)

client_socket.sendto(server_pings_no.encode(), (server_ip, int(server_port)))

recv_message, server_address = client_socket.recvfrom(2048)

print "Received server_pings_no: {}.\nFrom: {}".format(recv_message.decode(), server_address)

client_socket.close()

# 138.47.231.238
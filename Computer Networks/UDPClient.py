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
import sys
from datetime import datetime
import random
import time

client_socket = socket(AF_INET, SOCK_DGRAM)

ttl = 1
client_socket.settimeout(ttl)

server_ip = sys.argv[1]         # 192.168.1.6 during development
server_port = sys.argv[2]       # 12000
pings = sys.argv[3]

drops = 0
minimum = 0.0
maximum = 0.0
average = 0.0
times = []

now = datetime.now()
time_now = now.strftime("%c")

print "Pinging {}:".format(server_ip)

for i in range(0, int(pings)):
    try:
        message = "Ping {} {}".format(i+1, time_now)

        start_time = time.time()

        client_socket.sendto(message.encode(), (server_ip, int(server_port)))
        recv_message, server_address = client_socket.recvfrom(2048)

        end_time = time.time()

        total_time = round(1000 * (end_time - start_time), 1)

        if minimum > total_time:
            minimum = total_time
        elif maximum < total_time:
            maximum = total_time

        times.append(total_time)

    except timeout:
        print "Request timed out"
        drops += 1
        continue

    print "Reply from {}: {} time={}ms TTL={}".format(server_ip, recv_message.decode(), total_time, ttl)

pings = int(pings)
received = pings - drops

sum = 0.0
for t in times:
    sum += t

average = round(sum/len(times), 2)

loss = round(1 - float(received)/pings, 1) * 100

print "\nPing statistics for {}:".format(server_ip)
print "\tSegments: Send: {}, Received: {}, Lost: {} ({}%% Loss)".format(pings, received, drops, loss)
print "Approximate round trip times in ms:"
print "\tMinimum = {}ms, Maximum = {}ms, Average = {}ms".format(minimum, maximum, average)



client_socket.close()

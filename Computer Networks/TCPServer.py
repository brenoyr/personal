from socket import *

# create server socket
server_socket = socket(AF_INET, SOCK_STREAM)
# bind socket to port number
server_socket.bind(('', 12000))
# keep socket listening to connections
server_socket.listen(1)
print("Server is ready to receive...\n")

# get IP address
hostname = gethostname()    
IPAddr = gethostbyname(hostname)

# run forever loop to connect and receive messages
while(True):
    # create connection socket
    connection_socket, address = server_socket.accept()

    # receive message/request from connection socket
    incoming_message = connection_socket.recv(2048)
    incoming_request = incoming_message.decode()

    # print that request
    print "HTTP request to server:\nGET /{} HTTP/1.1\nHost: {}".format(incoming_request, IPAddr)
    print "\nObject to be fetched: {}".format(incoming_request)
    
    # try catch for if file requested doesn't exist
    try:
        # open file requested and include it in the message that will be sent back
        f = open(incoming_request)
        content = f.read()
        f.close()
        print "Object content:\n{}".format(content)
        message = "HTTP/1.1 200 OK\n\n" + content
    except IOError as e:
        message = "HTTP/1.1 404 Not Found"

    # print and sent the resulting message back to client
    print "\nHTTP response message:"
    print message
    connection_socket.send(message.encode())

    # close connection socket
    connection_socket.close()

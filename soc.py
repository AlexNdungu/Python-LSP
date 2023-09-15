import socket

# create a socket object
client_socket = socket.socket()

# get the hostname
host = "127.0.0.1"

# set the port number
port = 2087

# connection to hostname on the port.
client_socket.connect((host, port))

# receive data from the server
print(client_socket.recv(1024))

# close the client socket
client_socket.close()

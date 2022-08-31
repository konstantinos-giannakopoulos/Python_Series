import socket


### Create a socket
# AF_INET : internet socket
# UNIX : unix socket
# SOCK_STREAM : TCP protocol
# SOCK_DGRAM : UDP protocol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


### Create a server

#host = socket.gethostname()
host = ''
#print(host)
#host = socket.gethostbyname("127.0.0.1")
#host = socket.gethostbyname("localhost")
port = 9999
s.bind((host, port))
s.listen(5)
print("Listening...")

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    message = "Hello Client!"
    client.send(message.encode('ascii'))
    client.close()

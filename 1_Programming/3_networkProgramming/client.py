import socket


### Create a socket
# AF_INET : internet socket
# UNIX : unix socket
# SOCK_STREAM : TCP protocol
# SOCK_DGRAM : UDP protocol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


### Create a client

try:
    #host = socket.gethostname()
    #host = socket.gethostbyname("127.0.0.1")
    host = ''
    port = 9999
    s.connect((host, port))
    # try to receive up to 1024 bytes
    message = s.recv(1024)
    print(message.decode('ascii'))
except ConnectionRefusedError:
    print("ConnectionRefusedError: [Errno 61] Connection refused")
finally:
    s.close()


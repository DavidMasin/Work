import socket
my_socket = socket.socket()
my_socket.connect(('127.0.0.1',8821))
print("Connected to server")
input()
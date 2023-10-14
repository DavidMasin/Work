import socket
import time

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 8820))
message = input("Enter a message to send to the server: ")
time_start = time.time()
my_socket.send(message.encode())
print(my_socket.recv(1024).decode())
time_end = time.time()
print("The time it took to send and receive the message is: ", time_end - time_start)
my_socket.close()
import socket
my_socket = socket.socket()
my_socket.connect(("192.168.1.249", 8853))
my_socket.send("Omer".encode())
data = my_socket.recv(1024).decode()
print("The server sent " + data)
my_socket.close()

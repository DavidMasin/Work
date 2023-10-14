import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 8821))
(client_name, client_address) = server_socket.recvfrom(1024)
print("The client sent " + client_name.decode())
print("The client address is " + str(client_address))
data = client_name.decode()
response = "Hello " + data
server_socket.sendto(response.encode(), client_address)
server_socket.close()
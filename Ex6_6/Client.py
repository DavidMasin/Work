import socket
import time

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = time.time()
my_socket.sendto("Omer".encode(), ("127.0.0.1",8821))
(data, remote_address) = my_socket.recvfrom(1024)
end_time = time.time()
print("The time it took to send and receive the message is: ", end_time - start_time)
print("The server sent " + data.decode())
my_socket.close()
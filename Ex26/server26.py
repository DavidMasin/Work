"""EX 2.6 server implementation
   Author:
   Date:
"""
import datetime
import random
import socket
import protocol


def create_server_rsp(cmd):
    if cmd== "TIME":
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif cmd == "WHORU":
        return "David"
    elif cmd == "RAND":
        rand_number = random.randint(1, 10)
        return str(rand_number)
    return "Server response"


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)
        if valid_msg:
            # 1. Print received message
            # 2. Check if the command is valid
            # 3. If valid command - create response
            print(cmd)
            valid_cmd = protocol.check_cmd(cmd)
            if valid_cmd:
                response = create_server_rsp(cmd)
            else:
                response = "Wrong command"
        else:
            response = "Wrong protocol"
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage
        # Handle EXIT command, no need to respond to the client
        if cmd == "EXIT":
            server_socket.close()
            break
        # Send response to the client
        response_with_length = protocol.create_msg(response)
        client_socket.send(response_with_length.encode())

    print("Closing\n")
    # Close sockets


if __name__ == "__main__":
    main()

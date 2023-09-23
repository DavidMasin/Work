#   Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020

import glob
import os
import shutil
import socket
import subprocess

import pyautogui

import protocol

IP = "0.0.0.0"
PHOTO_PATH = "C:\\Users\\user\\Downloads\\screen.jpg"  # The path + filename where the screenshot at the server should be saved


def check_client_request(cmd):
    """
    Break cmd to command and parameters
    Check if the command and params are good.

    For example, the filename to be copied actually exists

    Returns:
        valid: True/False
        command: The requested cmd (ex. "DIR")
        params: List of the cmd params (ex. ["c:\\cyber"])
    """
    # Use protocol.check_cmd first
    # Then make sure the params are valid
    # (6)

    valid_cmd = protocol.check_cmd(cmd)
    if valid_cmd:
        if cmd == "SEND_PHOTO":
            return True, "SEND_PHOTO", [PHOTO_PATH]
        elif cmd == "TAKE_SCREENSHOT":
            return True, "TAKE_SCREENSHOT", [PHOTO_PATH]
        elif "DELETE" in cmd:
            return True, "DELETE", [cmd[7:]]
        elif "COPY" in cmd:
            parts = cmd.split()
            cmd = parts[0]
            paths = parts[1:]
            return True, cmd, [paths[0], paths[1]]
        elif "EXECUTE" in cmd:
            return True, "EXECUTE", [cmd[8:]]
        elif cmd == "EXIT":
            return True, "EXIT", []
        elif "DIR" in cmd:
            #print("Im here")
            return True, "DIR", [cmd[4:]]
    return False, "Error", []


def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_PHOTO, only the length of the file will be sent

    Returns:
        response: the requested data

    """
    # (7)
    response = ""
    print(command)
    print(params)
    if command == "DIR":
        response = glob.glob(rf"{params[0]}\*")
    elif command == "DELETE":
        print(params)
        os.remove(str(params[0]))
        response = "File deleted"
    elif "COPY" in command:
        print(params)
        print(command)
        shutil.copy(params[0], params[1])
        response = "File copied"
    elif command == "EXECUTE":
        subprocess.call(params[0])
        response = "Command executed"
    elif command == "TAKE_SCREENSHOT":
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(PHOTO_PATH)
        response = "Screenshot taken"
    elif command == "SEND_PHOTO":
        response = os.path.getsize(PHOTO_PATH)
    return response


def main():
    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    # (1)

    # handle requests until user asks to exit
    while True:
        # Check if protocol is OK, e.g. length field OK
        valid_protocol, cmd = protocol.get_msg(client_socket)
        print(cmd)
        print(valid_protocol)
        if valid_protocol:
            # Check if params are good, e.g. correct number of params, file name exists
            valid_cmd, command, params = check_client_request(cmd)
            print(valid_cmd)
            if valid_cmd:
                response = handle_client_request(command, params)
                massage = protocol.create_msg(response)
                print(massage)
                client_socket.send(protocol.create_msg(response))

                # (6)

                # prepare a response using "handle_client_request"

                # add length field using "create_msg"

                # send to client

                if command == 'SEND_FILE':
                    pass
                # Send the data itself to the client

                # (9)

                if command == 'EXIT':
                    break
            else:
                # prepare proper error to client
                response = 'Bad command or parameters'
                # send to client

        else:
            # prepare proper error to client
            response = 'Packet not according to protocol'
            server_socket.send(response.encode())
            # send to client

            # Attempt to clean garbage from socket
            client_socket.recv(1024)

    # close sockets
    print("Closing connection")


if __name__ == '__main__':
    main()

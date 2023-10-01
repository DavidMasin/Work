# Ex 4.4 - HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants
import os.path
# TO DO: import modules
import socket

# TO DO: set constants
IP = '127.0.0.1'
PORT = 80
SOCKET_TIMEOUT = 6


def get_file_data(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    DEFAULT_URL = '/80/index.html'

    if resource == '':
        url = DEFAULT_URL
    else:
        url = resource

    # TO DO: check if URL had been redirected, not available or other error code. For example:
    REDIRECTION_DICTIONARY = {'/': '/80/index.html', '/80/': '/80/index.html', '/index': '/80/index.html',
                              '/home': '/80/index.html', '/80/home': '/80/index.html', '/default': '/80/index.html'}
    if url in REDIRECTION_DICTIONARY:
        url = REDIRECTION_DICTIONARY[url]
        client_socket.send("HTTP/1.1 302 Found\r\n".encode())
        # TO DO: send 302 redirection response
    print(url)

    # TO DO: extract requested file tupe from URL (html, jpg etc)
    filetype = url.split('.')[-1]
    print(filetype)
    if filetype == 'html' or filetype == 'txt':
        http_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    elif filetype == 'jpg':
        http_header = "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n"
    elif filetype == 'js':
        http_header = "HTTP/1.1 200 OK\r\nContent-Type: text/javascript; charset=UTF-8\r\n\r\n"
    elif filetype == 'css':
        http_header = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n"
    else:
        http_header = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
    # TO DO: handle all other headers

    # TO DO: read the data from the file
    file_path = "C:\\Networks\\work\\EX4-4--HTTP\\webroot\\"

    filename = url.replace('/80', '',1)
    print("filename: " + filename)
    if filename == './80/':
        filename = 'index.html'
    print(file_path + filename)
    if (os.path.isfile(file_path + filename)):
        data = get_file_data(file_path + filename)  # add file_path before filename
        # print(data)
    else:
        http_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        data = b"<html><body><h1>404 Not Found</h1></body></html>"

    http_response = http_header.encode() + data  # encode http_header before concatenating with data
    print(http_header)
    client_socket.send(http_response)


def validate_http_request(request):
    # print(request)
    realRequest = request.split("\r\n")[0]
    partsOfRealRequest = realRequest.split(" ")
    # print(partsOfRealRequest)
    if len(partsOfRealRequest) != 3:
        return False, None
    if partsOfRealRequest[0] != 'GET' or partsOfRealRequest[2] != 'HTTP/1.1':
        return False, None
    return True, partsOfRealRequest[1]


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    # client_socket.send("Hello".encode())

    while True:
        client_request = client_socket.recv(1024).decode()
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            client_socket.send("HTTP/1.1 500 Internal Server Error\r\n\r\n".encode())
            print('Error: Not a valid HTTP request')
            break

    print('Closing connection')
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print(f"Listening for connections on port {PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()

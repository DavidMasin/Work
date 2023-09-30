import socket

IP = "127.0.0.1"
PORT = 80
hasClient = False


def connect():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port %d" % PORT)
    (client_socket, client_address) = server_socket.accept()
    print("New connection received")
    hasClient = True
    return client_socket, client_address


def disconnect(client_socket):
    client_socket.close()
    print("Connection terminated")
    hasClient = False


def getMessages(client_socket):
    data = client_socket.recv(1024).decode()
    if not ValidMessage(data):
        print("Invalid message received:" + data)
        disconnect(client_socket)
    return data


def ValidMessage(data):
    partsOfData = data.split(" ")
    if partsOfData[0] == "GET" and partsOfData[2] == 'HTTP/1.1':
        return True
    return False


def nameFile(data):
    partsOfData = data.split(" ")
    partOfURL = partsOfData[1].split("/")
    return partOfURL[len(partOfURL) - 1]


def sendFileName(client_socket, fileName):
    client_socket.send(fileName.encode())


def get_file_data(file_name):
    with open(file_name, 'rb') as f:
        return f.read()

def main():
    client_socket, client_address = connect()
    while hasClient:
        data = getMessages(client_socket)
        fileName = nameFile(data)
        sendFileName(client_socket, fileName)
        client_socket.send(get_file_data(fileName))
    disconnect(client_socket)

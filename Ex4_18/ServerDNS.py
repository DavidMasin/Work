import socket
import struct

DNS_SERVER_IP = '0.0.0.0'
DNS_SERVER_PORT = 53
DEAFULT_BUFFER_SIZE = 1024
TARGET_DOMAIN = 'www.c.com'
TARGET_IP = '192.0.2.123'


def dns_handler(data, addr):
    # Extract the transaction ID and domain name from the query
    TID = data[:2]
    idx = 12
    domain_name = ''
    while True:
        segment_length = data[idx]
        if segment_length == 0:
            break
        domain_name += data[idx + 1:idx + 1 + segment_length].decode() + '.'
        idx += 1 + segment_length

    domain_name = domain_name[:-1]  # Remove trailing dot

    # If the domain matches, create and send a response
    if domain_name == TARGET_DOMAIN:
        flags = struct.pack('>H', 0x8180)
        QDCOUNT = data[4:6]
        ANCOUNT = struct.pack('>H', 1)
        NSCOUNT = data[8:10]
        ARCOUNT = data[10:12]

        # Reuse the query part for the response
        query_part = data[12:idx + 1]

        # Construct the answer section
        response_part = query_part + struct.pack('>H', 1) + struct.pack('>H', 1) + struct.pack('>I',
                                                                                               3600) + struct.pack('>H',
                                                                                                                   4) + socket.inet_aton(
            TARGET_IP)

        # Construct the full response
        response = TID + flags + QDCOUNT + ANCOUNT + NSCOUNT + ARCOUNT + query_part + response_part

        server_socket.sendto(response, addr)


def dns_udp_server(ip, port):
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ip, port))
    print("Server started running successfully! Waiting for data...")
    while True:
        try:
            print("Waiting for client request...")
            data, addr = server_socket.recvfrom(DEAFULT_BUFFER_SIZE)
            print("Client request from: ", addr)
            print("Client request data: ", data)
            dns_handler(data, addr)
        except Exception as ex:
            print("Client exception! %s " % ex)


def main():
    print("DNS Server is running on port", DNS_SERVER_PORT)
    dns_udp_server(DNS_SERVER_IP, DNS_SERVER_PORT)


if __name__ == '__main__':
    main()

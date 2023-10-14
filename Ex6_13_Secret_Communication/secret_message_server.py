from scapy.all import *
from scapy.layers.inet import IP, UDP

secret_IP = "127.0.0.1"

def getLetter(ASCII_num):
    return chr(ASCII_num)


def filterMessage(packet):
    return UDP in packet and IP in packet and packet[IP].src == secret_IP


def reciveMessage():
    while True:
        print("Waiting for message...")
        my_packet = sniff(lfilter=filterMessage, count=1)
        print(my_packet)
        print(getLetter(my_packet[0][IP].dport), end="")

if __name__ == '__main__':
    reciveMessage()
from scapy.all import *
from scapy.layers.inet import IP

secret_IP = "127.0.0.1"


def getLetter(ASCII_num):
    return chr(ASCII_num)


def filterMessage(packet):
    return packet[IP].src == secret_IP


def reciveMessage():
    while True:
        packet = sniff(filter=filterMessage, count=1)
        print(packet)
        print(getLetter(packet[0][IP].dport), end="")
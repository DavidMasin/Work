from scapy.all import *
from scapy.layers.inet import IP, UDP

secret_IP = "127.0.0.1"
def get_ASCII_Num(letter):
    return ord(letter)

def getNewMessage():
    return input("Please write your secret message")

def sending(message):

    for i in message:
        packet = IP(dst = secret_IP)/UDP(dport = get_ASCII_Num(i))
        send(packet)


if __name__ == '__main__':
    sending(getNewMessage())
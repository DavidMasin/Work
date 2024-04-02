from scapy.all import *
from scapy.layers.inet import IP, UDP

secret_IP = "127.0.0.1"

def get_ascii_num(letter):
    return ord(letter)

def get_new_message():
    return input("Please write your secret message: ")

def send_message(message):
    for char in message:
        if 0 <= get_ascii_num(char) <= 127:
            packet = IP(dst=secret_IP) / UDP(dport=get_ascii_num(char))
            send(packet)
        else:
            print(f"Skipping non-ASCII character: {char}")

if __name__ == '__main__':
    send_message(get_new_message())

from scapy.all import *
from scapy.layers.inet import IP, UDP

secret_IP = "127.0.0.1"

def get_letter(ascii_num):
    if 0 <= ascii_num <= 127:
        return chr(ascii_num)
    return '?'  # Return a placeholder for non-ASCII values

def filter_message(packet):
    return UDP in packet and IP in packet

def receive_message():
    try:
        while True:
            print("Waiting for message...")
            my_packet = sniff(lfilter=filter_message, count=1)
            ascii_num = my_packet[0][UDP].dport
            print(get_letter(ascii_num), end="")
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    receive_message()

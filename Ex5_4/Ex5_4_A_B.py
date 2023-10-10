import time

from scapy.layers.dns import DNS, DNSQR
from scapy.all import *
from scapy.layers.inet import IP


def print_query_name(dns_packet):
    "This function prints the domain name from a DNS query"
    print(dns_packet[DNSQR].qname)


def filter_dns(packet):
    "This function filters query DNS packets"
    return (DNS in packet and packet[DNS].opcode == 0 and packet[DNSQR].qtype == 1 and packet[
        DNSQR].qname.decode() == 'www.google.com.')


print("Starting to sniff!")
my_packet = IP(dst="www.google.com") /"Hello world"
send(my_packet)
my_packet.show()

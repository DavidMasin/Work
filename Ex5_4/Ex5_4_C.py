import time
from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.dns import DNS, DNSQR

def print_query_name(dns_packet):
    """This function prints the domain name from a DNS query"""
    print(dns_packet[DNSQR].qname.decode('utf-8'))  # Decoding the byte-like object
    print(dns_packet.summary())

def filter_dns(packet):
    """This function filters query DNS packets"""
    return (
        DNS in packet and
        packet[DNS].opcode == 0 and
        packet[DNSQR].qtype == 1 and
        packet[DNSQR].qname.decode('utf-8') == 'www.facebook.com.'
    )

print("Starting to sniff!")
sniff(count=10, lfilter=filter_dns, prn=print_query_name)  # Note the usage of lfilter instead of filter

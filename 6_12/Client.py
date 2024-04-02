from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP


def resolve_domain_name(domain_name, dns_server='8.8.8.8'):
    dns_request = IP(dst=dns_server) / UDP(sport=RandShort(), dport=53) / DNS(rd=1, qd=DNSQR(qname=domain_name))

    response = sr1(dns_request, verbose=0)

    return response[DNS].an[0].rdata



if __name__ == '__main__':
    domain_name = input("Enter a domain name (e.g., www.google.com): ")
    dns_server = input("Enter a DNS server (default is 8.8.8.8): ")

    if not dns_server:
        dns_server = '8.8.8.8'

    ip_address = resolve_domain_name(domain_name, dns_server)

    if ip_address:
        print(f"The IP address of {domain_name} is {ip_address}")
    else:
        print(f"Failed to resolve the IP address for {domain_name}")

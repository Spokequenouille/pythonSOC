from scapy.all import *
import re

SQL_REGEX = re.compile(r'\b(select|insert|update|delete|drop|alter|create|truncate|grant|revoke|union|exec|fetch|open|close|declare|call)\b', re.IGNORECASE)


def handler(packet):
    if packet[TCP].dport==8000 or packet[TCP].dport == 443:
        if packet.haslayer(Raw):
            payload=packet[Raw].load.decode()
            if SQL_REGEX.search(payload):
                print("SQL")

sniff(iface="eth0", filter="tcp port 8000 or tcp port 443",prn=handler, count=10)
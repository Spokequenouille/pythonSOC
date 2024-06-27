from scapy.all import *
import re

SQL_REGEX = re.compile(r'\b(select|insert|update|delete|drop|alter|create|truncate|grant|revoke|union|exec|fetch|open|close|declare|call)\b', re.IGNORECASE)


def handler(packet):
    if packet.haslayer(TCP):
        if packet[TCP].dport==8000:
            if packet.haslayer(Raw):
                print(packet[Raw].load.decode())
                payload=packet[Raw].load.decode()
                if SQL_REGEX.search(payload):
                    print("SQL")

sniff(iface="eth0", filter="tcp port 8000",prn=handler)
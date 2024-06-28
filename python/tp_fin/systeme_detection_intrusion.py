from scapy.all import *
import re

SQL_REGEX = re.compile(r'\b(select|insert|update|delete|drop|alter|create|truncate|grant|revoke|union|exec|fetch|open|close|declare|call)\b', re.IGNORECASE)
XSS_REGEX = re.compile(r'\b(script|javascript|alert|fromcharcode|iframe)\b', re.IGNORECASE)

def handler(packet):
    if packet.haslayer(TCP):
        if packet[TCP].dport==8080:
            if packet.haslayer(Raw):
                payload=packet[Raw].load.decode()
                print(payload.split())
                request = payload.split()[1]
                if SQL_REGEX.search(request):
                    print("SQL")
                

sniff(iface="lo", filter="tcp port 8080",prn=handler)
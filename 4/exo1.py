import socket

from scapy.all import IP, TCP, sr1

def scan_port(ip, port):
    # Créer un paquet TCP avec SYN pour le port spécifié
    packet = IP(dst=ip) / TCP(dport=port, flags="S")
    # Envoyer le paquet et recevoir la réponse
    response = sr1(packet, timeout=1, verbose=0)
    # Analyser la réponse
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:  # SYN-ACK
            print(f"Port {port} est ouvert sur {ip}.")
        elif response[TCP].flags == 0x14:  # RST-ACK
            print(f"Port {port} est fermé sur {ip}.")
    else:
        print(f"Aucune réponse pour le port {port} sur {ip}.")


"""def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    if result == 0:
        print("port ouvert")
    else:
        print("port ferme")"""

def main():
    target_ip="10.125.26.76"
    start_port = 1
    end_port = 100
    for port in range(start_port,end_port+1):
        scan_port(target_ip,port)

import socket
from ipaddress import ip_address
from scapy.all import IP, TCP, sr1
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((str(ip),port))
    if result == 0:
        print(f"Le port {port} ouvert sur {ip}")
    else:
        print(f"Le port {port} ferme sur {ip}")
    sock.close()


def main():
    start_ip=ip_address("10.125.26.76")
    end_ip=ip_address("10.125.26.80")
    target_ip = start_ip
    start_port = 10
    end_port = 20
    with ThreadPoolExecutor(max_workers=100) as executor:
        while target_ip <= end_ip:
            for port in range(start_port,end_port+1):
                executor.submit(scan_port, target_ip, port)
                #scan_port(target_ip,port)
            target_ip+=1

main()
from scapy.all import IP, TCP, sr1, Ether, sendp, ARP, srp

ports = [22,80, 443]
target_ip = "192.168.201.134"
"""for port in ports:
    packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    if response and response.haslayer(TCP) and response[TCP].flags:
        print(f"Port {port} est ouvert sur {target_ip}.")
    else:
        print(f"Port {port} est fermé sur {target_ip}.")


packet = Ether()/IP(dst=target_ip)/TCP(dport=80, flags="S")
sendp(packet, loop=1, inter=0.1)
"""
arp = ARP(pdst=target_ip/20)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet)
result = srp(packet, timeout=3,verbose=1)[0]
for sent, receive in result:
    print(f"IP {receive.psrc}, MAC : '{receive.hwsrc}")
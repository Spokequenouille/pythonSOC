from scapy.all import ARP, sniff

def arp_spoof_detect(packet):
    if ARP in packet and packet[ARP].op == 2:
        print(packet)
        arp_table[packet[ARP].psrc] = packet[ARP].hwsrc

        if len(arp_table) > 1:
            ips = list(arp_table.keys())
            macs = list(arp_table.values())
            if len(set(macs)) > 1 and len(set(ips)) == 1:
                print(f"Alerte ! Possible ARP Spoofing détecté pour l'adresse IP: {ips[0]} avec les adresses MAC: {macs}")

arp_table = {}
print("Début de l'écoute des paquets ARP...")
sniff(filter="arp", prn=arp_spoof_detect, store=0)
from scapy.all import ARP, Ether, srp

def discover(network):
    arp_request = ARP(pdst=network)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame / arp_request

    result = srp(packet, timeout=2, verbose=1)[0]

    devices = []
    for sent, received in result:
        devices.append({"ip": received.psrc, "MAC": received.hwsrc})
    return devices

def main():
    network = "10.125.0.1/16"
    hosts = discover(network)
    print(hosts)

main()
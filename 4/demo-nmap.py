import nmap

def host_discovery():
    nmap_scanner = nmap.PortScanner()
    network = "10.125.26.0/24"
    nmap_scanner.scan(hosts=network, arguments="-sn")
    print("Hosts actifs : ")
    for host in nmap_scanner.all_hosts():
        if nmap_scanner[host].state() == "up":
            print(f"{host} est actif")


def port_scanner():
    nmap_scanner = nmap.PortScanner()
    host = "10.125.26.76"
    nmap_scanner.scan(host,'1-1024')
    for protocol in nmap_scanner[host].all_protocols():
        liste_ports = nmap_scanner[host][protocol].keys()
        for port in liste_ports:
            if nmap_scanner[host][protocol][port]["state"]=="open":
                print(f"Port {port} est ouvert")

def service_scanner():
    nmap_scanner = nmap.PortScanner()
    host = "10.125.26.76"
    nmap_scanner.scan(host,arguments="-sV")
    for protocol in nmap_scanner[host].all_protocols():
        liste_ports = nmap_scanner[host][protocol].keys()
        for port in liste_ports:
            service_info = nmap_scanner[host][protocol][port]
            print(f"Port : {port}/{[protocol]}")
            print(f"Service : {service_info['name']}")
            print(f"Version du service : {service_info['product']}, {service_info['version']}")

def host_os_discovery():
    nmap_scanner = nmap.PortScanner()
    network = "10.125.26.0/24"
    nmap_scanner.scan(hosts=network, arguments="-O")
    print("Hosts actifs : ")
    for host in nmap_scanner.all_hosts():
        if nmap_scanner[host].state() == "up":
            try:
                print(f"{host} est {nmap_scanner[host].hostname()}")
                os = nmap_scanner[host]["osmatch"][0]
                print(f"os est {os['name']} avec ")
            except Exception:
                print(Exception)
host_os_discovery()
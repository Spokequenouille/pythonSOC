import subprocess
import sys
import os
import json

# Fonction pour installer une bibliothèque si elle n'est pas déjà installée
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        __import__(package)

# Installation des bibliothèques nécessaires
install_and_import('nmap')
install_and_import('requests')
install_and_import('bs4')
install_and_import('vulners')

# Importation des bibliothèques après installation
import nmap
import requests
from bs4 import BeautifulSoup
import vulners

# Initialisation de l'API Vulners
vulners_api = vulners.Vulners(api_key=os.environ.get("VULNERS_KEY"))

# Fonction pour sauvegarder les vulnérabilités dans un fichier JSON
def save_vulnerabilities(service, vulnerability):
    with open(f"{service}.json", 'w') as file:
        json.dump(vulnerability, file, indent=4)

# Fonction pour scanner les adresses IP avec Nmap
def nmap_scan(target_ip, ports='80,443,3000,5000,8080,8000,8001,8081,8443,8888,9090'):
    scanner = nmap.PortScanner()
    scanner.scan(target_ip, ports, arguments='-sV')
    return scanner

# Fonction pour vérifier les vulnérabilités des services identifiés
def check_vulnerabilities(nmap_scanner, target_hosts):
    for host in target_hosts:
        for protocol in nmap_scanner[host].all_protocols():
            liste_ports = nmap_scanner[host][protocol].keys()
            for port in liste_ports:
                service_info = nmap_scanner[host][protocol][port]
                print(f"Port : {port}/{protocol}")
                print(f"Service : {service_info['name']}")
                print(f"Version du Service : {service_info['product']}, {service_info['version']}")
                if service_info['product'] and service_info['version']:
                    query = f"{service_info['product']} {service_info['version']}"
                    result_analys = vulners_api.search(query=query)
                    for vulnerability in result_analys:
                        save_vulnerabilities(service_info['name'], vulnerability=vulnerability)
                        print(f"{vulnerability['id']}  {vulnerability['title']}")

# Fonction pour vérifier si DVWA ou Juice Shop est présent
def check_vuln_app(scanner):
    vuln_hosts = []
    for host in scanner.all_hosts():
        print(f"Host : {host}")
        for proto in scanner[host].all_protocols():
            lport = scanner[host][proto].keys()
            for port in lport:
                state = scanner[host][proto][port]['state']
                if state == 'open':
                    url = f"http://{host}:{port}" if port not in [443, 8443] else f"https://{host}:{port}"
                    try:
                        response = requests.get(url, timeout=5)
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.content, 'html.parser')
                            title = soup.title.string if soup.title else 'No title'
                            print(f'Title: {title}')
                            if 'juice shop' in response.text.lower():
                                print(f'Juice Shop detected on {url}')
                                vuln_hosts.append(host)
                            elif 'dvwa' in response.text.lower():
                                print(f'DVWA detected on {url}')
                                vuln_hosts.append(host)
                    except requests.RequestException as e:
                        print(f'Could not retrieve content from {url}: {e}')
    return vuln_hosts

# Fonction principale
def main():
    target = "10.125.26.0/24"  # Remplacez par votre plage d'adresses IP
    scanner = nmap_scan(target_ip=target)
    vuln_hosts = check_vuln_app(scanner)
    if vuln_hosts:
        check_vulnerabilities(scanner, vuln_hosts)

if __name__ == "__main__":
    main()

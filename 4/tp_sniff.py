import subprocess
import sys

# Fonction pour installer une bibliothèque si elle n'est pas déjà installée
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Vérification et installation des bibliothèques nécessaires
install_and_import('nmap')
install_and_import('requests')
install_and_import('bs4')

# Importation des bibliothèques après installation
import nmap
import requests
from bs4 import BeautifulSoup

nm = nmap.PortScanner()

# Scanner le réseau pour les ports ouverts
nm.scan('10.125.26.0/24', '80,443,3000,5000,8080,8000,8001,8081,8443,8888,9090')

for host in nm.all_hosts():
    print(f'Host : {host}')
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            state = nm[host][proto][port]['state']
            if state == 'open':
                print(f'Port {port} is open on {host}')
                
                # Construire l'URL en fonction du port
                url = f"http://{host}:{port}" if port not in [443, 8443] else f"https://{host}:{port}"
                
                try:
                    # Envoyer une requête HTTP pour récupérer le contenu
                    response = requests.get(url, timeout=5)
                    if response.status_code == 200:
                        # Utiliser BeautifulSoup pour parser le contenu HTML
                        soup = BeautifulSoup(response.content, 'html.parser')
                        title = soup.title.string if soup.title else 'No title'
                        print(f'Title: {title}')
                        
                        # Vérifier si le contenu indique un Juice Shop ou un DVWA
                        if 'juice shop' in response.text.lower():
                            print(f'Juice Shop detected on {url}')
                        if 'dvwa' in response.text.lower():
                            print(f'DVWA detected on {url}')
                
                except requests.RequestException as e:
                    print(f'Could not retrieve content from {url}: {e}')

from scapy.all import *
import re
import json
import smtplib
from email.mime.text import MIMEText

SQL_REGEX = re.compile(r'\b(select|insert|update|delete|drop|alter|create|truncate|grant|revoke|union|exec|fetch|open|close|declare|call)\b', re.IGNORECASE)
LFI_REGEX = re.compile(r'(\.\./|\.\.\\|/etc/passwd|/bin/bash|/etc/shadow)', re.IGNORECASE)
DIR_TRAVERSAL_REGEX = re.compile(r'(\.\./|\.\.\\)', re.IGNORECASE)

def load_fichier(fichier):
    try:
        if os.path.exists(fichier):
            return open(fichier, "r")
        else:
            print("Le fichier n'existe pas")
            return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {fichier} : {e}")

def send_mail(attaque,log):
    try:
        config = json.load(load_fichier("conf_mail.json"))
        sender = config["email"]["sender"]
        password = config["email"]["password"]
        receivers = config["email"]["receivers"]
        body = f"Il y a eu une tentative d'attaque {attaque}\n{log}"
        msg = MIMEText(body)
        msg["Subject"]=f"Alerte tentative d'attaque {attaque}"
        msg["From"]=sender
        with smtplib.SMTP_SSL(config["other_settings"]["smtp_server"], config["other_settings"]["smtp_port"]) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, receivers, msg.as_string())
        print("Mail envoyé")
    except FileNotFoundError:
        print("Fichier de configuration des emails introuvable.")
    except Exception as e:
        print(f"Erreur lors de l'envoie du mail : {e}")


def handler(packet):
    if packet.haslayer(TCP):
        if packet[TCP].dport==80:
            if packet.haslayer(Raw):
                payload=packet[Raw].load.decode()
                print(payload.split())
                request = payload.split()[1]
                if SQL_REGEX.search(request):
                    print("SQL")
                    send_mail("SQL", payload)
                elif LFI_REGEX.search(request):
                    print("LFI")
                    send_mail("LFI", payload)
                elif DIR_TRAVERSAL_REGEX.search(request):
                    print("DIR traversal")
                    send_mail("Directory traversal", payload)

                
                

sniff(iface="eth0", filter="tcp port 80",prn=handler)
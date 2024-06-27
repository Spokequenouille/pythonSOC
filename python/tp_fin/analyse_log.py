import os
import matplotlib.pyplot as plt
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import json


def load_fichier(fichier):
    if os.path.exists(fichier):
        return open(fichier, "r")
    else:
        print("Le fichier n'existe pas")


def send_mail(nb_tentatives,ip):
    config = json.load(load_fichier("conf_mail.json"))
    sender = config["email"]["sender"]
    password = config["email"]["password"]
    receivers = config["email"]["receivers"]
    body = f"Il y a eu {nb_tentatives} tentatives de connexion depuis l'ip {ip}"
    msg = MIMEText(body)
    msg["Subject"]="Alerte tentative de connexion"
    msg["From"]=sender
    with smtplib.SMTP_SSL(config["other_settings"]["smtp_server"], config["other_settings"]["smtp_port"]) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, receivers, msg.as_string())
    print("Mail envoyé")

def ouverture_log():
    while True:
        fichier = input("Quel est le nom du fichier à ouvrir : ")
        fichier_ouvert = load_fichier(fichier)
        if fichier_ouvert != None:
            return fichier_ouvert

def filtrage_donnees(fichier):
    tentative_login = {}
    fichier_lignes = fichier.readlines()
    for ligne in fichier_lignes:
        ligne_tableau = ligne.split(',')
        evenement = ligne_tableau[3].strip()
        resultat = ligne_tableau[4].strip()
        if evenement == "login_attempt" and resultat=="FAILED":
            ip = ligne_tableau[2].strip()
            date_tentative = ligne_tableau[0].strip()
            print("Login failed")
            if ip in tentative_login:
                premiere_tentative, _ ,nb_tentatives = tentative_login[ip]
                tentative_login[ip] = (premiere_tentative, date_tentative ,nb_tentatives+1)
            else:
                tentative_login[ip] = (date_tentative, date_tentative, 1)
    return tentative_login

def visualisation(donnees):
    ips = list(donnees.keys())
    attempts = [donnees[ip][2] for ip in ips]
    file_name = "histogramme_"+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    plt.bar(ips, attempts, color='skyblue', width=0.8)
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.25)
    plt.xlabel("Adresses IP")
    plt.ylabel("Nombre de tentatives")
    plt.title("Histogramme des tentatives de connexion par adresse IP")
    plt.savefig(file_name)

def alerte(donnees):
    for ip, data in donnees.items():
        if data[2]>5:
            print(f"Il y a eu {data[2]} tentatives provenant de l'adresse {ip}, premiere en date : {data[0]}, derniere en date {data[1]}")
            send_mail(data[2],ip)

while True:
    fichier = ouverture_log()
    #fichier = open("analyse_log.txt","r")
    donnees = filtrage_donnees(fichier)
    visualisation(donnees)
    alerte(donnees)
    continuer = input("Voulez vous lire un autre fichier (o/n) : ").lower()
    if continuer != "o":
        break

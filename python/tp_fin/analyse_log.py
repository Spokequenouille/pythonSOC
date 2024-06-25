import os
import matplotlib.pyplot as plt

def ouverture_log():
    while True:
        fichier = input("Quel est le nom du fichier à ouvrir : ")
        print(fichier)
        if os.path.exists(fichier):
            return open(fichier, "r")
        else:
            print("Le fichier n'existe pas")

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
    plt.bar(ips, attempts, color='skyblue')
    plt.xlabel("Adresses IP")
    plt.ylabel("Nombre de tentatives")
    plt.title("Histogramme des tentatives de connexion par adresse IP")
    plt.savefig("test.png")

def alerte(donnees):
    for ip, data in donnees.items():
        if data[2]>1:
            print(f"Il y a eu {data[2]} tentatives provenant de l'adresse {ip}, premiere en date : {data[0]}, derniere en date {data[1]}")

while True:
    #fichier = ouverture_log()
    fichier = open("analyse_log.txt","r")
    donnees = filtrage_donnees(fichier)
    visualisation(donnees)
    alerte(donnees)
    break
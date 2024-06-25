import os
from datetime import datetime

rules = [
    ('ssh',22),
    ('http',80),
    ('https',443),
    ('rdp',3389),
    ('vnc',5900),
    ('tomcat',8080),
    ('jenkins',9090),
    ('mongodb',27017),
    ('web-app',8888),
    ('test-app',9999),
]

def ouverture_conf(fichier):
    while True:
        fichier = input("Quel est le nom du fichier à ouvrir : ")
        if os.path.exists(fichier):
            return open(fichier, "r")
        else:
            print("Le fichier n'existe pas")

def detection_anomalie(fichier):
    liste_anomalies = []
    fichier_ligne = fichier.readlines()
    for ligne in fichier_ligne:
        ligne_tableau = ligne.split()
        port = int(ligne_tableau[1].strip()[:-1])
        service = ligne_tableau[3].strip()[:-1]
        status = ligne_tableau[-1].strip()
        est_dans_rules=False
        for rule in rules:
            if rule[0]==service and rule[1]==port and status=='active':
                est_dans_rules=True
                break
        if est_dans_rules==False:
            liste_anomalies.append((service,port,status))
    return(liste_anomalies)

def creation_rapport(donnees):
    liste_rapport = []
    date = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    with open("rapport.txt",'w') as rapport:
        #liste_service = [rule[0] for rule in rules]
        for donnee in donnees:
            valide=False
            service, port, status = donnee
            for rule in rules:
                if service == rule[0]:
                    if port == rule[1]:
                        rapport.write(f"Le service {service} n'est pas actif, celui ci doit être lancé\n")
                    else:
                        if status=='active':
                            rapport.write(f"Le service {service} est actif sur le port {port}, celui ci doit être lancé sur le port {rule[1]}\n")
                        else:
                            rapport.write(f"Le service {service} n'est pas actif et celui ci est configuré sur un mauvais port {port}, il doit est activé et configuré sur le port {rule[1]}\n")
                    valide=True
                    break
            if valide==False:
                if status=="active":
                    rapport.write(f"Le service {service} est présent sur la machine au port {port}, il faut le désactiver et le supprimer\n")
                else:
                    rapport.write(f"Le service {service} est présent sur la machine au port {port} mais n'est pas actif, il faut le supprimer\n")
        

fichier = open("detection_configuration.txt", "r")
#fichier = ouverture_conf("detection_configuration.txt")
liste_anomalie = detection_anomalie(fichier)
creation_rapport(liste_anomalie)
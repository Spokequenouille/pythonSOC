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

def ouverture_conf():
    while True:
        fichier = input("Quel est le nom du fichier à ouvrir : ")
        if os.path.exists(fichier):
            try:
                with open(fichier, "r") as file:
                    return file.readlines()
            except Exception as e:
                print(f"Erreur lors de l'ouverture du fichier : {e}")
                continue
        else:
            print("Le fichier n'existe pas")

def detection_anomalie(fichier_ligne):
    liste_anomalies = []
    for ligne in fichier_ligne:
        try :
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
        except (IndexError, ValueError):
            print(f"Ligne malformée ignorée : {ligne.strip()}")
    return(liste_anomalies)

def creation_rapport(donnees):
    date = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    nom_rapport = f"rapport.txt_{date}"
    with open(nom_rapport,'w') as rapport:
        for donnee in donnees:
            rule_trouvee = False
            service, port, status = donnee
            for rule in rules:
                if service == rule[0]:
                    rule_trouvee=True
                    if port == rule[1]:
                        rapport.write(f"Le service {service} n'est pas actif, celui ci doit être lancé\n")
                    else:
                        if status=='active':
                            rapport.write(f"Le service {service} est actif sur le port {port}, celui ci doit être lancé sur le port {rule[1]}\n")
                        else:
                            rapport.write(f"Le service {service} n'est pas actif et celui ci est configuré sur un mauvais port {port}, il doit est activé et configuré sur le port {rule[1]}\n")
                    break
            if not rule_trouvee:
                if status=="active":
                    rapport.write(f"Le service {service} est présent sur la machine au port {port}, il faut le désactiver et le supprimer\n")
                else:
                    rapport.write(f"Le service {service} est présent sur la machine au port {port} mais n'est pas actif, il faut le supprimer\n")
    print(f"Rapport créé : {nom_rapport}")
fichier = ouverture_conf()
liste_anomalie = detection_anomalie(fichier)
creation_rapport(liste_anomalie)
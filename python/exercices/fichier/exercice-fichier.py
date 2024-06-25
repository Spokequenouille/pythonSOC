## Exercice : Journalisation des événements de sécurité
"""
**Objectif** : Créer un script Python qui enregistre des événements de sécurité dans un fichier. Chaque événement doit être horodaté avec la date et l’heure actuelles.

	1.	Vérifiez l’existence d’un fichier de journalisation nommé security_log.txt.
	- Si le fichier existe, ajoutez un nouvel événement avec la date et l’heure actuelles.
	- Si le fichier n’existe pas, créez-le et ajoutez le premier événement avec la date et l’heure actuelles.
	2.	Demandez à l’utilisateur de saisir une description de l’événement de sécurité.
	3.	Écrivez l’événement dans le fichier avec le format suivant :
  [YYYY-MM-DD HH:MM:SS] - Description de l'événement"""

import os
from datetime import datetime

fichier = "security_log.txt"

def ajout_log(log):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne_log = str(date) + " - " + log
    if os.path.exists(fichier):
        with open(fichier, 'a') as f:
            f.write(f'{ligne_log}\n')
    else:
        with open(fichier, 'w') as f:
            f.write(f'{ligne_log}\n')

while True:
    log = input("Saisir la ligne de log à ajouter au fichier : ")
    if len(log)==0:
        print("Fin du programme")
        break
    else: 
        ajout_log(log)
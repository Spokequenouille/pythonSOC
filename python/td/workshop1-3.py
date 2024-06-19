capacite_batterie = float(input("Capacité des batteries de secours (kWh) : "))
conso = float(input("Consommation moyenne du datacenter par heure (kW) : "))

duree_fonctionnement = capacite_batterie/conso
heure = int(duree_fonctionnement)
min= int((duree_fonctionnement-heure)*60)
print(f"Le serveur pourra fonctionner pendant : {heure} heures et {min} minutes")
conso = duree = None
while conso is None:
    try:
        conso = float(input("Consommation énergetique du datacenteur par heure (kW) : "))
    except ValueError:
        print("Valeur invalide, veuillez entrer un entier ou décimal")
while duree is None:
    try:
        duree = float(input("Durée de fonctionnement journaliere (h) : "))
    except ValueError:
        print("Valeur invalide, veuillez entrer un entier ou décimal")
        
print(f"Consommation journaliere : {conso*duree:0.2f}kW")
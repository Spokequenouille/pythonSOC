conso = None
while conso is None:
    try:
        conso = int(input("Consommation énergetique du datacenteur par heure (kW) : "))
    except ValueError:
        print("Invalid input, please enter an integer.")
duree = None
while duree is None:
    try:
        duree = int(input("Durée de fonctionnement journaliere (h) : "))
    except ValueError:
        print("Invalid input, please enter an integer.")

print(f"Consommation journaliere : {conso*duree}kW")
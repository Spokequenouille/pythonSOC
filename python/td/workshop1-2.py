cout = int(input("Cout par kWh : "))
conso = int(input("Consommation moyenne du systeme par heure : "))
duree = int(input("Durée de fonctionnement : "))

total = cout*conso*duree

print("Le cout total est de {}".format(total))
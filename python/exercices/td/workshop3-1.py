etat_serveurs=""
for i in range(1,6):
    etat = input(f"Le serveur {i} est il actif/inactif : ")
    etat_serveurs+=f"Le serveur {i} est {etat}\n"

print(etat_serveurs)
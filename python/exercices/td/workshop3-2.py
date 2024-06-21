serveurs_inactifs=""

for i in range(1,4):
    for j in range(1,4):
        etat_serveur=input(f"Est ce que le test de l'unité {i} a réussi (oui/non) : ").lower()
        if etat_serveur=="oui":
            print(f"L'unité {i} a réussi les tests la {j}e fois")
            break
        print(f"Le test {j} a échoué")
    if j==3:
        serveurs_inactifs+=f"Le serveur {i} nécessite une inspection manuelle\n"

print(serveurs_inactifs)

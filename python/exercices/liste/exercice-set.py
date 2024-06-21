noms_famille = set()

while True:
    choix = int(input(
"""
Que voulez vous faire :
1. Ajouter un nom
2. Afficher les noms
3. Editer un nom
4. Supprimer un nom
5. Quitter
Votre choix : """
))
    match choix:
        case 1:
            noms_famille.add(input("Nom de famille à ajouter : "))
        case 2:
            if len(noms_famille)>0:
                for elemnt in noms_famille:
                    print(elemnt)
            else:
                print("Pas de noms dans le set...")
        case 3:
            ancien_nom = input("Nom de famille à modifier : ")
            if ancien_nom in noms_famille:
                noms_famille.discard(ancien_nom)
                noms_famille.add(input("Le nouveau nom a enregister : "))
            else: 
                print("Le nom n'existe pas dans le set")
        case 4:
            nom_suppr = input("Nom de famille à supprimer : ")
            if nom_suppr in noms_famille:
                noms_famille.discard(nom_suppr)
            else:
                print("Le nom n'existe pas dans le set")
        case 5: 
            break
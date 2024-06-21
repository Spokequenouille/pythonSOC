### exercice

#Avec des variables de type dictionnaire dans une liste, vous réaliserez un logiciel pour stocker une série d'adresses avec : 
#- numéro de voie 
#- complément 
#- intitulé de voie 
#- commune 
#- code postal 
#- Pour ce faire, vous utiliserez des clés de type string qui représenteront les différentes lignes de l'adresse dans le dictionnaire. 
#- Le logiciel devra permettre l'ajout, l'édition, la suppression et la visualisation des données par l'utilisateur. 

liste_adresses = {}

while True:
    choix = int(input(
"""Que voulez vous faire :
1. Ajouter une adresse
2. Editer une adresse
3. Supprimer une adresse
4. Voir les adresses
5. Quitter
Votre choix : """))
    match choix:
        case 1:
            nom_adresse = input("Nom de l'adresse à ajouter : ")
            numero_voie = int(input("Numéro de la voie : "))
            intitule_voie = input("Intitulé de la voie : ")
            complement = input("Complement d'adresse : ")
            code_postal = input("Code postal : ")
            commune = input("Nom de la commune : ")
            liste_adresses[nom_adresse]={
                "numero_voie": numero_voie,
                "intitule_voie": intitule_voie,
                "complement": complement,
                "code_postal": code_postal,
                "commune": commune
                }
            print(f"L'adresse {nom_adresse} a bien été ajoutée")
        case 2:
            for element in liste_adresses:
                print(element)
            choix_edit = input("Quelle adresse modifier : ")
            if choix_edit in liste_adresses:
                numero_voie = int(input("Numéro de la voie : "))
                intitule_voie = input("Intitulé de la voie : ")
                complement = input("Complement d'adresse : ")
                code_postal = input("Code postal : ")
                commune = input("Nom de la commune : ")
                liste_adresses[choix_edit]={
                    "numero_voie": numero_voie,
                    "intitule_voie": intitule_voie,
                    "complement": complement,
                    "code_postal": code_postal,
                    "commune": commune
                }
                print(f"L'adresse {choix_edit} a bien été modifiée")
        case 3:
            for element in liste_adresses:
                print(element)
            choix_suppr = input("Quelle adresse supprimer : ")
            if choix_suppr in liste_adresses:
                liste_adresses.pop(choix_suppr)
            print(f"L'adresse {choix_suppr} a bien été suprimée")
        case 4:
            for element in liste_adresses:
                print(element)
            choix_affiche = input("Quelle adresse afficher : ")
            if choix_affiche in liste_adresses:
                print(f"""{element}
{liste_adresses[choix_affiche].get('numero_voie')} {liste_adresses[choix_affiche].get('intitule_voie')}
{liste_adresses[choix_affiche].get('complement')}
{liste_adresses[choix_affiche].get('code_postal')} {liste_adresses[choix_affiche].get('numero_voie')}""")
        case 5:
            break
        case _:
            continue
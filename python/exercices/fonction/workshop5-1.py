utilisateurs={}

def ajouter_utilisateur(nom: str, role: str):
    #correction prof :
    #if nom not in utilisateurs:
        #utilisateurs[nom]=role
    utilisateurs[nom]=role

def changer_role(nom,role):
    if nom in utilisateurs.keys():
       utilisateurs[nom]=role
       print("L'utilisateur a ete modifie")
    else:
       print("L'utilisateur n'existe pas")

def afficher_utilisateurs():
    for nom, role in utilisateurs.items():
        print(f"L\'utiliseur {nom} est {role}")
    #for user in utilisateurs:
    #    print(f"L\'utilisateur {user} est {utilisateurs[user]}")

while True:
    choix = int(input("""Que voulez vous faire : 
1. Ajouter un utilisateur
2. Changer le role d'un utilisateur         
3. Afficher les utilisateurs
4. Quitter
Votre choix : """))
    match choix:
        case 1:
            nom = input("Le nom de l'utilisateur à ajouter : ")
            role=""
            #while role!="administrateur" and role!="visiteur" and role!="operateur":
            while role not in ["administrateur", "visiteur", "operateur"]:
                role = input("Quel est le role de l'utilisateur : ").lower()
            ajouter_utilisateur(nom,role)
        case 2:
            nom = input("Le nom de l'utilisateur à modifier : ")
            #while role!="administrateur" and role!="visiteur" and role!="operateur":
            while role not in ["administrateur", "visiteur", "operateur"]:
                role = input("Quel est le role de l'utilisateur : ").lower()
            changer_role(nom,role)
        case 3:
            afficher_utilisateurs()
        case 4:
            break
        case _:
            print("Choix invalide, veuillez réessayer")
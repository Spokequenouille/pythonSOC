taches_maintenance = [(1,"Jouer","Parce que","en cours")]

def recherche_par_id(id):
    for i, tache in enumerate(taches_maintenance):
        if tache[0]==id:
            return i
    return None

def ajouter_tache(id,tache,description,statut):
    if recherche_par_id(id) is None:
        print("Tache ajoutée")
        taches_maintenance.append((id,tache,description,statut))
    else:
        print(f"La tache {id} existe déjà")

def mettre_a_jour_tache(id,nouveau_statut):
    res = recherche_par_id(id)
    if res is None:
        print(f"L'id {id} n'existe pas dans la liste de taches")
    else:
        id,tache,description,statut = taches_maintenance[res]
        taches_maintenance[res]=((id,tache,description,nouveau_statut))
        """for i, tache_modif in enumerate(taches_maintenance):
            if id == tache_modif[0]:
                id,tache,description,statut=tache_modif
                taches_maintenance[i]=((id, tache,description,nouveau_statut))
                print("Tache modifiée")
                return  """
while True:
    print(taches_maintenance)
    choix = int(input("""Que voulez vous faire
1. Ajouter une tache
2. Mettre à jour une tache
3. Quitter
Votre choix : """))
    match choix:
        case 1:
            id = int(input("Id de la tache :  "))
            tache = input("Nom de la tache : ")
            description = input("Description de la tache : ")
            statut = ""
            while (statut.lower() != "en cours") and (statut.lower() != "termine"):
                statut=input("Etat de la tache (En cours/Termine) : ")
            ajouter_tache(id,tache,description,statut)
        case 2:
            id = int(input("Id de la tache à modifier : "))
            statut=""
            while (statut.lower() != "en cours") and (statut.lower() != "termine"):
                statut=input("Etat de la tache (En cours/Termine) : ")
            mettre_a_jour_tache(id,statut)
        case 3:
            break
        case _:
            print("Choix invalide, veuillez réessayer")
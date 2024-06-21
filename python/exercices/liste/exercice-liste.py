liste_notes = []

choixSaisie = input("Connaissez vous le nombre de notes à saisir (o/n) : ").lower()
if choixSaisie=='n':
    while True:
        note = int(input(f"Note : "))
        if note < 0:
            break
        else:
            liste_notes.append(note)
else:
    nb_note = int(input("Nombre de notes a entrer : "))
    for i in range(nb_note):
        liste_notes.append(int(input(f"Note {i} : ")))

while True:
    choixAffichage=int(input(
"""Que voulez vous voir: 
1. La note maximale
2. La note minimale
3. La moyenne des notes
4. Quitter
Votre choix : """))
    match choixAffichage:
        case 1:
            print(f"La note maximale est : {max(liste_notes)}")
            #max=None
            #for i in liste_notes:
            #   max=i if i>max 
        case 2:
            print(f"La note minimale est : {min(liste_notes)}")
        case 3:
            print(f"La moyenne des notes est : {sum(liste_notes)/len(liste_notes)}")
        case 4:
            break
        case _:
            print("Choix inconnu...")
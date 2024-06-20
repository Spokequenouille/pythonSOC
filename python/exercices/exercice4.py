nb_photocopie = int(input("Nombre de photocopies à faire : "))
prix_photocopie=0

if nb_photocopie<10:
    prix_photocopie = round(nb_photocopie*0.15,2)
elif nb_photocopie<20:
    prix_photocopie = round(nb_photocopie*0.10,2)
else:
    prix_photocopie = round(nb_photocopie*0.05,2)

print(f"Le cout pour {nb_photocopie} sera de {prix_photocopie}€")
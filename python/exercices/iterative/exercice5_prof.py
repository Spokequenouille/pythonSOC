#None parce que ca reduit l'espace en mémoire + on sait pas si il va mettre que des négatifs
plus_grand_nombre = None

print("Merci de saisir 20 nombres")

for i in range(20):
    nombre_saisi = float(input(f"Nombre {i+1}: "))
    if plus_grand_nombre is None or nombre_saisi > plus_grand_nombre:
        plus_grand_nombre = nombre_saisi
#supprime espace memoire pour var 1
del i

print(f"Le plus grand nombre est {plus_grand_nombre}")
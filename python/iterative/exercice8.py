import math

nb = int(input("Entrez un nombre : "))
#OK j'abuse un peu
#print(math.factorial(nb))
nb_fact=1
for i in range(nb):
    nb_fact*=(i+1)
print(f"La factorielle de {nb} est {nb_fact}")
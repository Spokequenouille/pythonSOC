import math

nb = int(input("Entrez un nombre : "))
nb_abs = abs(nb)
#OK j'abuse un peu
#print(math.factorial(nb))
nb_fact=1
for i in range(1,nb_abs+1):
    nb_fact*=(i)
if nb<0 and nb%2==1:
    nb_fact = -nb_fact
print(f"La factorielle de {nb} est {nb_fact}")
"""nbmax = 0
for i in range(20):
    nb=int(input("Saisissez un nombre : "))
    if(nb > nbmax): nbmax=nb
    
print(f"Le nombre le plus grand est {nbmax}")"""

nbmax=0
for _ in range(5):
    nbmax=max(nbmax,int(input("Saississez un nombre : ")))
print(nbmax)

#opti de fou
#nbmax = max(int(input("Saississez un nombre : ")) for _ in range(20))
#print(nbmax)
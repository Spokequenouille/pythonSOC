nbmax = 0
for i in range(20):
    nb=int(input("Saisissez un nombre : "))
    if(nb > nbmax): nbmax=nb
    
print(f"Le nombre le plus grand est {nbmax}")
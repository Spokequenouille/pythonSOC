nbmax = 0
pos = 0
for i in range(20):
    nb=int(input("Saisissez un nombre : "))
    if(nb > nbmax): 
        nbmax=nb
        pos = i+1
    
print(f"Le nombre le plus grand est {nbmax}. Il est en position {pos}")
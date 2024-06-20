value = int(input("Veuillez saisir une valeur : "))
tempvalue = 1
 
for i in range (1,value+1):
    tempvalue = tempvalue + (tempvalue * (value - i))
 
print(f"la factorielle de votre valeur est : {tempvalue}")
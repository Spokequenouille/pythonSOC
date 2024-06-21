nb = int(input("Saississez un nombre : "))
nb_long_max = len(str(nb*10))+3
for i in range(1,nb+1):
    ligne=""
    for j in range(1,11):
        num=f"{i*j}"
        num+=(" "*(nb_long_max-len(num)))
        ligne+=num
    print(ligne)
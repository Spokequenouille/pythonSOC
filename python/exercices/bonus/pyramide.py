nb = int(input("Saississez un nombre : "))

for i in range(1,nb+1):
    ligne=""
    for j in range(1,11):
        num=f"{i*j}"
        num+=(" "*(5-len(num)))
        ligne+=num
    print(ligne)
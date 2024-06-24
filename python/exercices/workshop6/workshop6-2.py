def somme(liste_nombre):
    return sum(liste_nombre)
    #res = 0
    #for i in liste_nombre
        #res+=i
    #return res

def moyenne(liste_nombre):
    return sum(liste_nombre)/len(liste_nombre)
    #res_sum = 0
    #for i in liste_nombre:
        #res_sum+=i
    #return res_sum/len(liste_nombre)

def produit(liste_nombre):
    res = 1
    for i in range(len(liste_nombre)):
        res*=liste_nombre[i]
    return res

def calcul(*args, **kwargs):
    operations = {
        'somme': lambda list: sum(list),
        'moyenne': lambda list: sum(list)/len(list),
        'produit': lambda list: (lambda res = 1: [res := res * num for num in list][-1])(1)
        }

    operation=kwargs.get("operation")
    """match operation:
        case "somme":
            print()
        case "moyenne":
            print(moyenne(args))
        case "produit":
            print(produit(args))
        case _:
            print("Operation non reconnue")"""
    if operation in operations:
        print(operations[operation](args))
    else:
        print("Operation npn reconnue")
    

calcul(1,2,3,4,5,6,7,8,9, operation="somme")
calcul(1,2,3,4,5,6,7,8,9, operation="moyenne")
calcul(1,2,3,4,5,6,7,8,9, operation="produit")
calcul(0, operation="produit")
calcul(1,9, operation="produit")



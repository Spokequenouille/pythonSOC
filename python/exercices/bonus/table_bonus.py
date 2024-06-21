ligne = int(input("Hauteur du triange : "))
longueur = (ligne*2)-1
for i in range(1,ligne+1):
    nb_etoile=(i*2)-1
    espace=(longueur-nb_etoile)
    print((" "*(espace//2))+("*"*nb_etoile)+(" "*(espace//2)))
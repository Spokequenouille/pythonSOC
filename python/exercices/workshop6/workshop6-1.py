etat_serveurs = [("serveur 1",70),("serveur 2",20), ("serveur 3",50),('BDD',40)]

"""def trier_serveurs(**kwargs):
    print(kwargs)
    value = kwargs.get("clef_tri")
    print(value)
    etat_sort=""
    if value == "nom":
        print("nom")
        etat_sort = sorted(etat_serveurs, key=lambda x: x[0])
    elif value=="utilisation_cpu":
        print("cpu")
        etat_sort = sorted(etat_serveurs, key=lambda x:x[1])
    print(etat_sort)
"""

"""def trier_serveurs(**kwargs):
    print(kwargs)
    serveurs = kwargs.get("serveur")
    cle_tri = kwargs.get("clef_tri")
    if cle_tri == "nom":
        key= lambda x:x[0]
    elif cle_tri == "utilisation_cpu":
        key = lambda x:x[1]
    else:
        print("Clef non reconnue")
        return
    cmp = lambda x,y:x>y
    switch = lambda x,y: (y,x)
    for i in range(len(serveurs)):
        for j in range(0, len(serveurs)-i-1):
            if cmp(key(etat_serveurs[j]), key(etat_serveurs[j+1])):
                etat_serveurs[j], etat_serveurs[j+1] = switch(etat_serveurs[j], etat_serveurs[j+1])
    print(etat_serveurs)
    """

def trier_serveurs(**kwargs):
    print(kwargs)
    serveurs = kwargs.get("serveur")
    cle_tri = kwargs.get("clef_tri")
    if cle_tri == "nom":
        key= lambda x:x[0]
    elif cle_tri == "utilisation_cpu":
        key = lambda x:x[1]
    else:
        print("Clef non reconnue")
        return
    liste_trie = []
    print(liste_trie)

trier_serveurs(serveur = etat_serveurs, clef_tri="nom")
trier_serveurs(serveur = etat_serveurs, clef_tri="utilisation_cpu")
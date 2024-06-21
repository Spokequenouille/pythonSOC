ressource_disponibles = int(input("Quelle est la quantité de ressources disponibles : "))
ressource_processus = int(input("Quelle est la quantité de ressources demandées par le processus : "))

print("Les ressources peuvent être alloués") if ressource_processus<=ressource_disponibles else print("Le ressources ne peuvent pas être alloués")
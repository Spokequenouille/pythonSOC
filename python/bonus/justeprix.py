import random

def juste_prix():
    prix_min = 1
    prix_max = 1000
    
    prix_a_deviner = random.randint(prix_min, prix_max)
    
    print("Bienvenue au Juste Prix !")
    print(f"Devinez le prix compris entre {prix_min} et {prix_max}.")

    tentative = 0
    
    while True:
        try:
            proposition = int(input("Entrez votre proposition : "))
            tentative += 1
            
            if proposition < prix_a_deviner:
                print("C'est plus haut !")
            elif proposition > prix_a_deviner:
                print("C'est plus bas !")
            else:
                print(f"Félicitations ! Vous avez trouvé le juste prix de {prix_a_deviner} en {tentative} tentatives.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        
if __name__ == "__main__":
    juste_prix()

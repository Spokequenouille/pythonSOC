# Écrire un programme de caisse qui permet à l'utilisateur de saisir le prix de plusieurs articles un par un.
# Lorsqu'un prix de 0 est saisi, cela signifie la fin des saisies.
# Le programme doit ensuite afficher le total à payer, demander à l'utilisateur le montant de son paiement,
# et calculer et afficher la monnaie à rendre,
# en décomposant cette monnaie en billets de 10 euros, 5 euros, et en pièces de 1 euro.

prix_total=0
prix=1
while(prix!=0):
    prix=int(input("Indiquez le prix de l'article (0 si fin) : "))
    prix_total+=prix

print(f"Prix total : {prix_total}")
montant_paye=0
while montant_paye<prix_total:
    montant_paye = int(input("Inserer le montant de votre paiement : "))

dif_paiement = montant_paye - prix_total
"""billet10 = dif_paiement//10
dif_paiement -= 10*billet10
billet5 = dif_paiement//5
dif_paiement -= 5*billet5
piece1 = dif_paiement//1
"""
billet10=0
billet5=0
piece1=0
while (dif_paiement>=10):
    billet10+=1
    dif_paiement-=10
while (dif_paiement>=5):
    billet5+=1
    dif_paiement-=5
while (dif_paiement>0):
    piece1+=1
    dif_paiement-=1

print(f"""Monaie rendue : {montant_paye-prix_total}
      {billet10} Billets de 10
      {billet5} Billets de 5
      {piece1} Pieces de 1""")
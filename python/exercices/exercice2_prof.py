age = int(input("Donne moi ton age : "))
salaire = int(input("Donne moi ton salaire : "))
experience = int(input("Donne moi ton experience : "))

valide = True
message = ""

if age<30:
    message+="Vous n'avez pas l'age minimum\n"
    valide=False
if salaire>40000:
    message+="Vous demandez trop d'argent\n"
    valide=False
if experience<5:
    message+="Vous n'avez pas assez d'expérience"
    valide=False

if valide:
    message = "Votre candidature a été retenue"

print(message)
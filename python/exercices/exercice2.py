age = int(input("age : "))
salaire = int(input("salaire : "))
experience = int(input("experience : "))

if age<30:
    print("Trop jeune")
elif salaire>40000:
    print("salaire trop élevé")
elif experience<5:
    print("pas assez d'expérience")
else:
    print("ok")
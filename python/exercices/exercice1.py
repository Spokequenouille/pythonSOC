temp = float(input("Entrez un temperature (°C) : "))

if temp<0:
    print("L'eau est à l'état solide")
elif temp <= 100:
    print("L'eau est à l'état liquide")
else:
    print("L'eau est à l'état gazeux")
nb = int(input("saisire un nombre entier : "))

print(f"Le nombre {nb} est divisible par 3") if nb%3==0 else print(f"Le nombre {nb} n'est pas divisible par 3")

print(f"Le nombre {nb} est divisible par 3") if not(nb%3) else print(f"Le nombre {nb} n'est pas divisible par 3")

"""if nb%3==0:
    print(f"Le nombre {nb} est divisible par 3")
else:
    print(f"Le nombre {nb} n'est pas divisible par 3")
"""
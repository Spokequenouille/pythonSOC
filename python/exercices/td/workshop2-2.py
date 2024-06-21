import unidecode

niveau_incident_utilisateur = input("Saississez le niveau de gravité de l'incident (Faible, Modéré, élevé): ")

match unidecode.unidecode(niveau_incident_utilisateur.lower()):
    case "faible":
        print("Contacter le soc n1")
    case "modere":
        print("Contacter le soc n2")
    case "eleve":
        print("Contacter le soc n3")
    case _:
        print("Qu'est ce que tu me baragouine ?!")
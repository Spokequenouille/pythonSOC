'''liste_de_logs = {"ERROR":["JSP","coucou","c'est chelou"],"INFO":["j'ai faim","j'ai soif", "dormir","zzzzzzzz"]}
#liste_de_logs = {}

def filter_logs(niveau_prio):
    logs = liste_de_logs[niveau_prio]
    for log in logs:
        print(f"{niveau_prio} : {log}")

def compter_logs():
    niveau_prio = liste_de_logs.keys()
    if len(niveau_prio)==0:
        return None
    retour_logs={}
    for l in niveau_prio:
        retour_logs[l]=len(liste_de_logs[l])
    return retour_logs

while True:
    choix=int(input("""Que voulez vous faire : 
1. Filtre les logs
2. Comter le nombre de logs 
3. Quitter
Votre choix : """))
    match choix:
        case 1:
            niveau_prio = ""
            while niveau_prio not in ["ERROR", "INFO"]:
                niveau_prio=input("Quels logs voulez vous voir (ERROR, INFO): ").upper()
            filter_logs(niveau_prio)
        case 2:
            logs = compter_logs()
            if logs is None:
                print("Il n'y a pas de logs")
            else:
                for niveau, nombre_logs in logs.items():
                    print(f"Il y a {nombre_logs} logs de niveau {niveau}")
        case 3:
            break
        case _:
            print("Choix invalide")'''

liste_de_logs=["INFO : test", "ERROR : c'est chaud", "INFO : hey salut", "WARNING : ouais salut c'est greg"]

def filtrer_logs(niveau_prio):
    logs_filtre = []
    for log in liste_de_logs:
        if log.startswith(niveau_prio):
            logs_filtre.append(log)
    return logs_filtre
            

def compter_logs():
    res = {"INFO":0, "WARNING":0, "ERROR":0}
    for log in liste_de_logs:
        if log.startswith("INFO"):
            res["INFO"]+=1
        elif log.startswith("WARNING"):
            res["WARNING"]+=1
        elif log.startswith("ERROR"):
            res["ERROR"]+=1
        else:
            print(f"Log inconnu {log}")
    return res

while True:
    choix=int(input("""Que voulez vous faire : 
1. Filtre les logs
2. Comter le nombre de logs 
3. Quitter
Votre choix : """))
    match choix:
        case 1:
            niveau_prio = ""
            while niveau_prio not in ["ERROR", "INFO", "WARNING"]:
                niveau_prio=input("Quels logs voulez vous voir (ERROR, INFO, WARNING): ").upper()
            resultat = filtrer_logs(niveau_prio)
            for res in resultat:
                print(res)
        case 2:
            logs = compter_logs()
            for niveau, nombre_logs in logs.items():
                print(f"Il y a {nombre_logs} logs de niveau {niveau}")
        case 3:
            break
        case _:
            print("Choix invalide")
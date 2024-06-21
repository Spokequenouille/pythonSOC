"""cpt_latence_consecutif=0
while True:
    latence=(input("Quelle est la latence actuelle du réseau : "))
    if latence=="stop":
        if latence.lower()=="stop":
            print("Fin de la surveillance")
            break
    else:
        if int(latence)>100:
            cpt_latence_consecutif+=1
            print("Avertissement : La latence est trop élevée...")
            if cpt_latence_consecutif==3:
                print("Alerte : Il y a un problème sur le réseau, arret... ")
                break
        else:
            cpt_latence_consecutif=0"""

cpt_latence_consecutif=0
while True:
    latence=(input("Quelle est la latence actuelle du réseau : "))
    is_lettre=False
    """for i in latence:
        if i not in ("0","1","2","3","4","5","6","7","8","9"):
            is_lettre=True
            break
    if is_lettre:
        print("lettre")
        if latence=="stop":
            break"""
    if not latence.isdigit():
        if latence=="stop":
            print("Fin de la surveillance")
            break
    else:
        if int(latence)>100:
            action_corrective=input("Une action corrective a t elle été prise (oui/non) : ")
            if action_corrective.lower()=="non":
                cpt_latence_consecutif+=1
                print("Avertissement : La latence est trop élevée...")
                if cpt_latence_consecutif==3:
                    print("Alerte : Il y a un problème sur le réseau, arret... ")
                    break
        else:
            cpt_latence_consecutif=0
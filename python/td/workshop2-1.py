bandeTotale = int(input("Bande passante totale disponible (Gbps) : "))

nb_services = int(input("Nombre de services : "))

services=[]
for i in range(nb_services):
    nom_service=input(f"Nom du service {i+1} : ")
    prio_service=int(input(f"Priorité du service {nom_service}(max: 1, min: 3) :"))
    bande_service_demande=int(input(f"Bande passante du service {nom_service} : "))
    bande_service_donnee = 0
    services.append([nom_service,prio_service, bande_service_demande, bande_service_donnee])

services = sorted(services, key=lambda service: service[1])
print(services)

bande_demande_totale = sum(i[2] for i in services)
print(bande_demande_totale)

if bande_demande_totale > bandeTotale:
    priorite_totale = sum((4-i[1]) for i in services)
    print("prio totale",priorite_totale)
    #osef de la demande de base
    for s in services:
        s[3]=bandeTotale*(4-s[1])/priorite_totale
        print(s)
    #proportionel au lvl et la demande de base
    total_pondere = sum(((4-i[1])*i[2]) for i in services)
    for s in services:
        s[3]=bandeTotale*((4-s[1])/total_pondere*s[2])
        print(s)
else:
    for service in services:
        service[3]=service[2]

for i in services:
    print(i)
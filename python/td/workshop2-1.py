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
    priorite_totale = sum(i[1] for i in services)
    print(priorite_totale)
    diff_bande_passante = bande_demande_totale - bandeTotale
    for service in services:
        service[3]=service[2]-(diff_bande_passante((3-service[1]+1)/nb_services))
        print((3-service[1]+1)/priorite_totale)
        print(f"Le service {service[0]} a {service[3]} Gbps de bande passante")

    #jsp si je diminue tout le monde, ou si je valide les priorités 1 et apres je modifie les autres
else:
    for service in services:
        service[3]=service[2]
        print(f"Le service {service[0]} a {service[3]} Gbps de bande passante")
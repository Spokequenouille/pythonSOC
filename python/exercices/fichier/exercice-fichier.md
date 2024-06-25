## Exercice : Journalisation des événements de sécurité

**Objectif** : Créer un script Python qui enregistre des événements de sécurité dans un fichier. Chaque événement doit être horodaté avec la date et l’heure actuelles.

	1.	Vérifiez l’existence d’un fichier de journalisation nommé security_log.txt.
	- Si le fichier existe, ajoutez un nouvel événement avec la date et l’heure actuelles.
	- Si le fichier n’existe pas, créez-le et ajoutez le premier événement avec la date et l’heure actuelles.
	2.	Demandez à l’utilisateur de saisir une description de l’événement de sécurité.
	3.	Écrivez l’événement dans le fichier avec le format suivant :
  [YYYY-MM-DD HH:MM:SS] - Description de l'événement
### TP : Création d'un Utilisateur avec des Contraintes de Sécurité Avancées sur le Mot de Passe

#### Etape 1 -> Les contraintes :

Nombre de tentatives autorisées pour entrer un mot de passe correct.
Longueur minimale du mot de passe.
Nombre de caractères différents par rapport au mot de passe précédent.
Au moins une lettre majuscule.
Au moins une lettre minuscule.
Au moins un chiffre.
Au moins un caractère spécial.
Nombre maximal de répétitions consécutives de caractères.
Nombre maximal de répétitions consécutives de classes de caractères.
Vérifie si le mot de passe contient le nom complet de l'utilisateur.

### Étape 2 -> Créer un Nouvel Utilisateur et Tester les Contraintes de Sécurité
 
Créez un nouvel utilisateur appelé `testuser` :

### Bonus : Paramètres supplémentaires de `pam_pwquality.so`

Voici quelques paramètres supplémentaires que vous pouvez utiliser pour affiner les règles de sécurité :

Rend les règles de mot de passe obligatoires.
Spécifie le chemin vers un fichier de dictionnaire pour vérifier les mots de passe contre des mots communs.

Modifiez ces paramètres à la ligne `pam_pwquality.so` dans `/etc/pam.d/common-password` si nécessaire.
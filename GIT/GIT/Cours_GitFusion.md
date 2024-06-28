## Fusionner les branches (merge/rebase)

Lorsque j'ai fini de travailler sur ma branche, je voudrais souvent appliquer mon travail à la branche principale (main).
Cette étape est possible grâce à la **fusion de branches**. Mais il existe plusieurs types de fusion possible:

## Le `merge`:

Le merge crée un nouveau commit de fusion *(merge commit)* qui combine les modifications de la branche source dans la branche de destination. Ce commit de fusion a deux parents: un pour la branche source et un pour la branche de destination.

Le merge préserve l'historique des commits de manière linéaire et montre clairement quand et d'où proviennent les modifications.

Il est recommandé pour les collaborations où plusieurs contributeurs travaillent sur la même branche, car il préserve l'histoire des contributions individuelles.

**Pour réaliser un merge, je me place dans ma branche de destination et j'utilise `git merge`**

```bash
# Par exemple, si je veux fusionner ma branche "feature1" avec ma branche "main"

# Je me place dans ma branche main qui va recevoir les changements
git switch main

# Je fusionne ma branche feature1
git merge feature1
```

Le merge peut rencontrer deux cas de figures: Avec ou sans fast-forward.

- **Le "fast-forward" (avance rapide):**
Il s'agit d'une méthode de fusion particulière qui se produit lorsque Git peut intégrer les modifications d'une branche dans une autre sans créer de commit de fusion supplémentaire. Le fast-forward est possible lorsque les conditions suivantes sont remplies:
    - Vous avez une branche de destination et une branche source.
    - La branche source contient des commits que la branche de destination n'a pas encore incorporés
    - Les commits de la branche source sont linéaires par rapport à la branche de destination, c'est à dire qu'ils s'ajoutent les uns après les autres dans l'ordre chronologique.

Cela donne l'apparence d'une fusion propre et linéaire dans l'historique des commits. Le FF est souvent préféré lorsque c'est possible, car il maintient la clarté sans créer de commits de merges supplémentaires. Cependant, il n'est pas toujours applicable, en particulier lorsque des divergences importantes existent entre les branches à fusionner. Je peux forcer la non-utilisation d'un FF (par exemple si je veux volontairement un merge commit) en ajoutant l'option `--no-ff` (`git merge nom_branche --no-ff`)

- **Sans fast-foward:**
Lorsque des divergences existent entre les deux branches, je ne peux pas simplement "coller" ma  branche source à ma branche de destination. Un commit de fusion *(merge commit)* est donc créé. Ce commit de fusion héritera des deux branches et n'existera qu'au sein de la branche de destination.
C'est dans cette configuration qu'un **conflit** peut apparaître.
En effet, si une même ligne est modifié dans les deux parents, Git devra faire un choix dans ce qu'il récupère, c'est donc à l'utilisateur de reprendre la main pour faire ce choix et **résoudre** le conflit. 
VSCode utilise un outil graphique pour réparer les conflits mais vous pouvez utiliser le `git mergetool` pour régler les conflits en CLI.
Si ces conflits ne sont pas voulus, **je peux annuler mon merge** grâce à l'option `--abort`
```bash
git merge --abort
```

## Le `rebase`

Il existe une autre méthode pour fusionner deux branches: le rebase

- Le rebase réapplique séquentiellement chaque commit de la branche source sur **le dessus** de la branche de destination. Il "rejoue" l'historique des commits, ce qui donne l'apparence d'une ligne de temps linéaire et propre.

- **Il ne crée pas de commits de fusion supplémentaires.** Les commits originaux de la branche sources sont réécrits avec de nouvelles valeurs de hachage.

- Le rebase peut être utilisé pour garder l'historique des commits plus propre et plus linéaire, mais il peut réécrire l'historique des commits, ce qui peut causer des conflits si plusieurs contributeurs travaillent sur la même branche.

- C'est une stratégie généralement recommandée pour les branches locales où vous voulez garder votre historique propre et pour intégrer régulièrement les mises à jour à la branche principale (main).

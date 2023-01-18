# Trackdéchets préparation inspection

## Utilitaire de préparation de fiches d'inspection

Dépôt de code du projet **Trackdéchets préparation inspection** incubé à la Fabrique Numérique du Ministère de la
Transition Écologique.

## Installation

Initialisation et activation d'un environnement

```
$ pipenv shell
```

### Installation des dépendances

```
$ pipenv install -d
```

### Environnement

Se référer au fichier src/core/settings/env.dist

### Tests

Cf. config/settings/tests.py

Créer :
- un rôle postgre `inspection`
- une db postgre `inspection_test`

Lancer les tests avec :

```
$ pytest
```


### Linting (python + templates)

Utiliser :

```
    $ ./lint.sh
```

## Licence

Le code source du logiciel est publié sous licence [MIT](https://fr.wikipedia.org/wiki/Licence_MIT).

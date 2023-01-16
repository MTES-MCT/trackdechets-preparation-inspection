# Trackdéchets préparation inspection

## Utilitaire de préparation de fiches d'inspection

Dépôt de code du projet **Trackdéchets préparation inspection** incubé à la Fabrique Numérique du Ministère de la Transition Écologique.


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

### Linting

Utiliser : 

```
    $ ./lint.sh
```

et pour les templates :

```
    $ djlint templates --profile=django --reformat
```

## Licence

Le code source du logiciel est publié sous licence [MIT](https://fr.wikipedia.org/wiki/Licence_MIT).

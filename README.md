# Trackdéchets préparation inspection

## Utilitaire de préparation de fiches d'inspection

Dépôt de code du projet **Trackdéchets préparation inspection** incubé à la Fabrique Numérique du Ministère de la
Transition Écologique.

## Prérequis:

- Une instance de prosgresql récente avec l'extension postgis installée
- Une instance redis
- Python >= 3.11 avec pipenv
- les librairies nécessaires aux fonctionalités géographiques de django (GDAL et GEOS)

## Installation

Initialisation et activation d'un environnement

```
$ pipenv shell
```

### Installation des dépendances

```
$ pipenv install -d
```

### Variable d'environnement

2 db sont nécessaires:
- DATABASE_URL, managée par django, pour les comptes, les données calculées etc.
- WAREHOUSE_URL, en lecture seule, contenant un dump des données du data warehouse Trackdéchets

Se référer au fichier env.dist

### Setup de la db

Lancer la commande de migration:

```
    $ manage.py migrate
```

Créer un super utilisateur

```
    $ manage.py createsuperuser
```

### Lancement de l'application

```
    $ manage.py runserver
```

Pour les tâches asynchrones, dans une autre fenêtre de terminal:

```
    $ DJANGO_SETTINGS_MODULE='config.settings.dev' celery -A config worker -l info
```

### Installation des dépendances front

A la racine du projet :

```
    $ npm install
```

### Lancement de l'UI de cartographie

Dans un second terminal, 

```
    $ npm run dev
```

### Utilitaires

Pour lancer un rendu de manière synchrone (et glisser plus facilement des breakspoints):

```
    $ manage.py prepare_sheet <sheet_pk>
```


Pour récupérer les établissements depuis le data warehouse:

```
    $ manage.py retrieve_companies
```


### Tests

Cf. config/settings/tests.py

Créer :
- un rôle postgre `inspection`
- une db postgre `inspection_test`

Lancer les tests avec :

```
    $ pytest
```

### Création en masse d'utilisateurs

Un template xls est disponible à la racine. 
Un fois rempli le fichier est importable par la section users de l'interface d'admin (via django-import-export).

### Linting (python + templates)

Utiliser :

```
    $ ./lint.sh
```

Linter de scanning de sécurité

```
    $ bandit -c pyproject.toml -r
```

## Licence

Le code source du logiciel est publié sous licence [MIT](https://fr.wikipedia.org/wiki/Licence_MIT).

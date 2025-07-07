# Contribuer

## Profils utilisateurs

Les profils `is_staff`ont des droits particuliers.
Les droits des autres profils sont détérminés par le champ `user_category`:

- les profils observatoires n'ont accès qu'à la page observatoires
- les autres profils ont accès à tout sauf la page observatoires
- chaque vue héritant du mixin `FullyLoggedMixin` doit renseigner la variable `allowed_user_categories` par une liste de
  catégories autorisées ou par
  `["*"]` si la vue est accessible à tous les utilisateurs.

## Authentification

Une authentification à 2 facteurs est mise en place grâce à django-otp et les EmailDevice

Workflow:

- L'utilisateur se connecte normalement avec email/mdp (user.is_authenticated est True)
- Un email contenant un code secret lui est adressé, le code a une durée de vie de `OTP_EMAIL_TOKEN_VALIDITY` secondes (
  10 min par défaut)
- Il est dirigé vers la page du second facteur
- Il renseigne le code reçu. Il est désormais vérifié ( user.is_verified() est True )
- Les views à protéger héritent de FullyLoggedMixin qui requiert un user vérifié ou connecté via Monaiot
- L'admin django est également protégé
- L'utilisateur peut demander un renvoi de code. L'envoi est throttlé (`OTP_EMAIL_THROTTLE_DELAY` secondes) via une key
  redis pour éviter les abus.

## Open ID Connect

Les utilisateurs concernés peuvent se connecter via un workflow open ID connect depuis ProConnect et MonAIOT

## Téléchargement de fichier parquets

Des fichiers parquet sont déposés régulièrement sur un hébergement s3 privé (les fichiers ne sont pas accessibles au
public).
La commande `manage.py retrieve_data_exports` permet de parcourir le bucket concerné et de récupérer les paths, noms,
années
et tailles des exports pour reseigner les modèles `DataExport`. Les modèles `DataExport`
permettent d'afficher la page de listing.
Au clic, une url présignée est générée et renvoyée à l'utilisateur qui télécharge ainsi le fichier recherché.

## Purge des fiches établissements

Les fiches établissement consomment beaucoup d'espace db. La commande `manage.py void_sheets` vide le contenu des fiches
de plus de 90
jours tout en conservant l'historique.

## Permissions

| Profil                      | Fiche + registre | Contrôle routier | Bordereau | Cartographie | Observatoires | 🆕 Cartographie des exutoires | Accès admin |
|-----------------------------|------------------|------------------|-----------|--------------|--------------|-------------------------------|-------------|
| **Staff Track déchets**     | ✅                | ✅                | ✅         | ✅            | ✅            | ✅                             | ✅           |
| **Administration centrale** | ✅                | ✅                | ✅         | ✅            | ✅            | ✅                             | ❌           |
| **Inspecteur ICPE**         | ✅                | ✅                | ✅         | ✅            | ❌            | ✅                             | ❌           |
| **CTT**                     | ✅                | ✅                | ✅         | ✅            | ❌            | ❌                             | ❌           |
| **Inspection du travail**   | ✅                | ❌                | ✅         | ✅            | ❌            | ❌                             | ❌           |
| **Gendarmerie**             | ✅                | ✅                | ✅         | ✅            | ✅            | ✅                             | ❌           |
| **ARS**                     | ✅                | ❌                | ✅         | ✅            | ❌            | ❌                             | ❌           |
| **Douanes**                 | ✅                | ✅                | ✅         | ✅            | ❌            | ❌                             | ❌           |
| **Observatoires**           | ❌                | ❌                | ❌         | ✅            | ✅            | ❌                             | ❌           |

## Bannière configurable

Une bannière éditable visible sur toutes les pages est configurable depuis l'admin dans "Site configuration"



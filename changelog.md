# Changelog

Les changements importants de Trackdéchets préparation inspection sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et le projet suit un schéma de versionning inspiré de [Calendar Versioning](https://calver.org/).

## 20/06/2023
- Ajout des composants multi-variables pour les quantités.
## 07/06/2023
- Ajout des données de contenants pour les BSFF.
## 30/05/2023
- Ajout d'une table listant les bordereaux présentant des quantités aberrantes.
## 29/05/2023
- Ajout d'une table listant les BSDA de déchets collectés chez des particuliers.
## 25/05/2023
- Corrige le problème de certains tableaux qui étaient coupés en version PDF.

## 17/05/2023
- Ajout des statistiques sur les déchets non dangereux suivis par BSDD.
- Utilise les m3 comme unité pour les DASRIs.

## 16/05/2023
- Ajout du temps de traitement moyen pour les bordereaux qui ont un traitement d'une durée supérieure à un mois.

## 11/05/2023
- Ajout d'un formulaire d'enquête.


## 04/05/2023
- Ajout d'un composant permettant de lister les bordereaux (BSDD et BSDA) pour lesquels l'établissement se positionne en tant qu'émetteur et destinataire et qui ont une adresse travaux renseignée.


## 03/05/2023
- Ajout de filtre de dates sur tous les data processors pour être sûr que les données soient 
comprises dans une fenêtre d'une année glissante.

## 20/04/2023
- Ajout d'un composant listant les bordereaux annulés.

## 03/04/2023
- Ajoute un composant permettant de lister les déchets indiqués comme dangereux mais qui n'ont pas de code déchets dangereux

## 30/03/2023
- Corrige la gestion des date manquantes sur le tableau icpe [#3](https://github.com/MTES-MCT/trackdechets-preparation-inspection/pull/3)
- Améliore le composant de statistiques déchets [#4](https://github.com/MTES-MCT/trackdechets-preparation-inspection/pull/4)
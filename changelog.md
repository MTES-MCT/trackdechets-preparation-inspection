# Changelog

Les changements importants de Trackdéchets préparation inspection sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
et le projet suit un schéma de versioning inspiré de [Calendar Versioning](https://calver.org/).

## 04/07/2024

- Amélioration du dashboard

## 01/07/2024

- Ajout des requêtes de révision pour les BSDASRI

## 23/06/2024

- mise en place de l'Api

## 21/06/2024

- Ajout des données ICPExRNDTS
- Prise en charge du transport multi-modal pour le BSFF

## 27/05/2024

- Ajout des données du RNDTS

## 10/04/2024

- Téléchargement du registre Trackdéchets

## 08/04/2024

- Connexion via mon aiot

## 28/03/2024

- Ajout des révisions en cours pour chaque type de bordereau

## 20/02/2024

- Réorganisation de la mise en page ;
- Le filtre de date sur les données est maintenant plus précis ;
- La Fiche Inspection est renommée en Fiche Établissement.

## 29/01/2024

- Ajout des données sur le transport transfrontalier de déchets

## 04/01/2024

- Passage à python 3.11 et django 5, mise à jour des dépendances

## 11/12/2023

- Ajout de statistiques pour les transporteurs

## 04/12/2023

- Ajout de statistiques pour les entreprise de travaux

## 09/11/2023

- Mise à jour du mode d'emploi

## 31/10/2023

- Ajout d'un second facteur pour la connexion (code reçu par email)

## 25/09/2023

- Ajout d'un composant permettant d'avoir la liste des établissements reliés par le même SIREN.
- Ajout de la date de création de l'établissement.

## 12/09/2023

- Ajout d'un composant alertant lorsqu'un établissement traite des déchets dangereux
  sans avoir les bonnes rubriques ICPE ou en l'absence de données ICPE.

## 06/09/2023

- Ajout de nouveaux composants permettant de suivre les données ICPE de l'établissement.

## 07/08/2023

- Ajout de la possibilité de choisir l'intervalle de dates pour lequel afficher les données.

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

# Outil de traitement de corpus

## Tâche:
L'objectif principal de ce projet est de classifier les images de chiens. Plus précisément, nous souhaitons identifier et classifier trois races différentes de chiens présentes dans le jeu de données.

## Corpus utilisé:

https://www.kaggle.com/datasets/mohamedchahed/dog-breeds

## Description du Corpus
Nous utilisons un corpus d'images de différentes races de chiens, structuré comme suit :
- Les fichiers d'images bruts sont stockés dans le répertoire `data/raw`
- Les formats d'images incluent `.jpg`
- Chaque image a une étiquette correspondante

Le corpus contient un nombre total d'images, réparties en trois races de chiens, avec un nombre d'images à peu près égal pour chaque race.

## Type de Prédiction
Ce corpus est principalement utilisé pour des tâches de classification d'images, permettant d'entraîner un modèle pour prédire la race du chien représentée dans une image.


## Les modèles et techniques pourrait être adapté pour travailler avec ce corpus

1. Réseaux de Neurones Convolutionnels (CNN) pour la classification des races
2. Apprentissage par Transfert pour utiliser des modèles pré-entraînés sur des ensembles de données plus larges et les adapter à la reconnaissance des races spécifiques

## Informations Supplémentaires sur le Corpus

- **Prétraitement des Données** : Avant l'entraînement, nous avons normalisé les images et les avons redimensionnées à une taille uniforme (224x224).
- **Extraction de Caractéristiques** : Utilisation de couches convolutionnelles pour extraire les caractéristiques des images.
- **Augmentation des Données** : Utilisation de transformations aléatoires (rotation, translation, zoom) pour augmenter les données d'entraînement et améliorer la capacité de généralisation du modèle.



## Scripts
**1.recuperer_les_donnees.py**: récupérer automatiquement des données depuis le web

**2.generate_csv.py**: convertir le corpus au format Dataset (les même colonnes que le corpus de référence)

**3.statistique.ipynb**: les statistiques adaptées au corpus, visualisation les statistique de corpus

**4.traitement_evaluation.ipynb**: 

- Mesurer la correlation entre deux variables 

- Eliminer les données abérrantes

- Augmenter les données

- Splitter le corpus en test et train

- Evaluer le corpus avec les métriques adaptées

- Proposer une métrique pour le corpus autre que les métriques de la tâche





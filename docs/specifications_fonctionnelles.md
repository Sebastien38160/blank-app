# Spécifications fonctionnelles de l'application Streamlit d'analyse de données de jeux vidéo

## Introduction

Cette application Streamlit permet aux utilisateurs d'explorer et de visualiser les données de vente de jeux vidéo. Elle vise à fournir une interface conviviale pour analyser les tendances du marché et faciliter la prise de décisions.

## Diagramme de cas d'utilisation

```mermaid
graph TD
    A[Utilisateur] --> B(Inscription);
    A --> C(Connexion);
    A --> D(Téléchargement de fichier CSV);
    A --> E(Exploration des données);
    A --> F(Visualisation des données);
    A --> G(Paramètres);

## Impact mapping    
graph TD
    A[Objectif : Faciliter l'analyse des données de vente de jeux vidéo] --> B{Acteurs};
    B --> C[Analystes de données];
    B --> D[Étudiants];
    B --> E[Passionnés de jeux vidéo];
    A --> F{Impacts};
    F --> G[Améliorer la compréhension des tendances du marché];
    F --> H[Faciliter la prise de décisions];
    A --> I{Livrables};
    I --> J[Tableaux de bord interactifs];
    I --> K[Rapports personnalisés];

## Schéma d'arborescense
graph TD
    A[Accueil] --> B[Exploration des données];
    A --> C[Visualisation des données];
    A --> D[Paramètres];

Spécifications détaillées
Exploration des données
Entrées : Fichier CSV téléchargé par l'utilisateur, filtres sélectionnés par l'utilisateur.
Traitements : Lecture du fichier CSV, application des filtres, calcul des statistiques descriptives.
Sorties : Tableau de données filtrées, statistiques descriptives.
Règles de gestion : Validation du format du fichier CSV, gestion des valeurs manquantes.
Cas d'erreur : Fichier CSV invalide, erreur de lecture du fichier.
Visualisation des données
Entrées : Données sélectionnées par l'utilisateur, type de graphique choisi par l'utilisateur.
Traitements : Création du graphique à partir des données sélectionnées.
Sorties : Graphique interactif.
Règles de gestion : Gestion des types de données compatibles avec chaque type de graphique.
Cas d'erreur : Données incompatibles avec le type de graphique choisi.
Interface utilisateur
Boutons pour télécharger des fichiers CSV, appliquer des filtres, afficher des graphiques, etc.
Champs de texte pour saisir des filtres.
Graphiques interactifs pour visualiser les données.
# Étape 1 : Structure de Données Portfolio - Votre fondation concrète

## 📊 Developer Story
Vous démarrez votre tableau de bord financier. Au lieu de travailler avec des données abstraites, vous voulez commencer avec un vrai portefeuille d'actions. Vous avez un fichier CSV avec vos positions actuelles et vous voulez le charger en Python pour commencer à travailler avec des données réelles dès le début.

## 🎯 Concept : Manipulation de fichiers et données structurées
Python excelle dans la manipulation de fichiers de données. Les modules `csv` et `json` permettent de lire facilement des fichiers de données. Utilisez les modules `csv` et `json` pour importer les données dans un Portfolio nommé `portfolio_sample`

## 📚 Ressources utiles
- [Documentation Python CSV](https://docs.python.org/3/library/csv.html)
- [Documentation Python JSON](https://docs.python.org/3/library/json.html)

## 🎯 Objectif
**Créez une base de données portfolio concrète qui servira pour TOUS les exercices suivants.**

## 📝 Exercice
Créez `portfolio_loader.py` avec les fonctions essentielles :

### Fonctions requises :
1. **`lire_portfolio_csv(nom_fichier)`** - charge le portfolio depuis `portfolio_sample.csv`
2. **`lire_portfolio_json(nom_fichier)`** - charge le portfolio depuis `portfolio_sample.json`
3. **`afficher_portfolio(portfolio)`** - affiche un résumé lisible du portfolio

### Fonction optionnelle :
4. **`sauvegarder_portfolio(portfolio, nom_fichier)`** - sauvegarde les modifications

## 💰 Votre Portfolio de Départ
Vous disposez de ces fichiers :
- **`portfolio_sample.csv`** : Format simple pour débutants
- **`portfolio_sample.json`** : Format structuré avec métadonnées

**Contenu du portfolio** :
- AAPL (Apple) : 10 actions à 150€
- GOOGL (Google) : 5 actions à 2500€  
- MSFT (Microsoft) : 20 actions à 300€
- TSLA (Tesla) : 8 actions à 800€
- NVDA (Nvidia) : 15 actions à 400€
- AMZN (Amazon) : 12 actions à 100€
- META (Meta) : 25 actions à 200€

**Valeur totale initiale : 47 000€**

## ✅ Solution attendue
- Code propre avec les fonctions essentielles
- la fonction pour créer un portfolio depuis un fichier csv ou json

## 🚀 Pour aller plus loin
- Ajoutez une fonction de recherche par symbole
- Validez les données lors du chargement
- Ajoutez support pour d'autres formats (Excel, XML)

Ce portfolio concret sera utilisé dans TOUS les exercices suivants.


# Étape 4 : La Fonction Map - Traiter tout votre portfolio d'un coup

## 📊 Developer Story
Maintenant que vous avez vos calculs lambda, vous voulez les appliquer à TOUT votre portfolio en une seule opération. Au lieu de faire une boucle for pour chaque calcul sur chaque action, vous voulez une méthode élégante pour traiter toutes les positions simultanément.

## 🎯 Concept : Map appliqué à un portfolio réel
La fonction `map()` applique automatiquement vos lambdas financières à toutes les positions de votre portfolio. C'est parfait pour calculer la valeur de chaque position, les gains de chaque action, ou tout autre métrique sur l'ensemble de votre portefeuille en une seule ligne.

## 📚 Ressources utiles
- [Comment utiliser map() : quelques exemples](https://www.enki.com/post/apply-a-function-to-each-element-in-a-list---python-s-map-function)
- [Real Python - la fonction map()](https://realpython.com/python-map-function/)


## 🎯 Objectif
**Utilisez map() pour appliquer vos calculs financiers à l'ensemble de votre portfolio en une fois.**

## 📝 Exercice
Créez `portfolio_map.py` avec des fonctions de traitement global :

### Fonctions requises :
1. **`calculer_valeurs_positions(positions)`** - utilise map() pour calculer la valeur de chaque position
2. **`calculer_gains_portfolio(positions, prix_actuels_dict)`** - calcule tous les gains d'un coup
3. **`calculer_rendements_portfolio(positions, prix_actuels_dict)`** - calcule tous les rendements

### Fonction optionnelle :
4. **`generer_rapport_complet(positions, prix_actuels_dict)`** - rapport de performance global


## ✅ Solution attendue
- les fonctions pour le calcul des valeurs, gains et rendements
- **25-40 lignes** utilisant map() systématiquement


### Prix actuels simulés
Utilisez le fichier Utilisez portfolio_actual_prices_sample.csv pour récupérer des prix actuels simulés
### Résultats attendus pour le portfolio exemple:
```
Valeurs d'achat : [1500.0, 12500.0, 6000.0, 6400.0, 6000.0, 1200.0, 5000.0]
Gains actuels : [250.0, 500.0, 400.0, -400.0, 750.0, 120.0, -500.0]
Rendements : [16.7, 4.0, 6.7, -6.25, 12.5, 10.0, -10.0]
```

## 🔍 Points d'attention
1. **Conversion** : N'oubliez pas `list()` autour de `map()`
2. **Performance** : map() est plus rapide qu'une boucle for sur de gros portfolios

## 🚀 Pour aller plus loin
- Combinez map() avec filter() pour traiter seulement les positions gagnantes
- Utilisez map() pour convertir les prix USD en EUR
- Créez une fonction qui applique plusieurs calculs avec map()

## 🔄 Utilité pour la suite
Ces traitements en lot seront utiles pour les graphiques et l'interface web !


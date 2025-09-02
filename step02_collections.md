# Étape 2 : Collections - Structurer votre portfolio avec les collections

## 📊 Developer Story
Maintenant que vous pouvez charger votre portfolio depuis des fichiers, vous vous rendez compte que manipuler des dictionnaires partout (`data['symbol']`, `data['quantity']`) devient fastidieux et source d'erreurs. Vous voulez une structure de données plus propre et plus sûre pour représenter vos positions d'actions.

## 🎯 Concept : Les Collections spécialisées
Le module Python `collections` fournit des conteneurs de données spécialisés. `namedtuple` crée des objets légers avec des champs nommés (comme une classe simple mais plus rapide). Vous pouvez accéder aux données avec `position.symbol` au lieu de `dictionnaire['symbol']`. C'est plus lisible, plus rapide, et moins d'erreurs de frappe !


## 📚 Ressources utiles
- [Documentation Python collections](https://docs.python.org/3/library/collections.html)
- [Real Python - Guide sur namedtuple](https://realpython.com/python-namedtuple/)

## 🎯 Objectif
**Transformez votre portfolio en structures de données propres et type-safe avec namedtuple.**

## 📝 Exercice
Créez `portfolio_structures.py` qui améliore votre étape 1 :

### Éléments requis :
1. **Position** - prend un symbole, une quantité, un prix d'achat et une date d'achat
2. **Transaction** - prend une date, un symbole, une quantité, un prix et un type (achat ou vente)
3. **Classe Portfolio** - A vous de voir sa structure.
3. **`Position = namedtuple(...)`** - structure pour chaque action du portfolio
4. **`convertir_vers_positions(portfolio_dict)`** - convertit les dictionnaires en namedtuples
5. **`afficher_positions(positions)`** - affiche avec la nouvelle structure

## ✅ Solution attendue
- **40-60 lignes** incluant les structures, la conversion et l'affichage
- Code plus lisible : `position.symbol` au lieu de `data['symbol']`
- Adaptation de votre fonction d'affichage de l'Étape 1

## 🔍 Points d'attention
1. **Immutabilité** : Les namedtuple ne peuvent pas être modifiés après création
2. **Types de données** : Assurez-vous que quantity est int et purchase_price est float
3. **Compatibilité** : Vos fonctions de l'Étape 1 doivent être adaptées
4. **Votre choix de structure de données est important, soignez-le !**

## 🚀 Avantages
- **Autocomplétion** : Votre IDE propose automatiquement `.symbol`, `.quantity`
- **Performance** : Plus rapide que les dictionnaires
- **Code plus propre** : Plus lisible et maintenable

## 🔄 Impact sur la suite
Toutes les étapes suivantes utiliseront ces structures !


# Étape 3 : Les Fonctions Lambda - Calculs financiers sur votre portfolio

## 📊 Developer Story
Maintenant que votre portfolio est bien structuré avec des namedtuples, vous voulez créer des calculs financiers simples et réutilisables. Pour chaque position de votre portfolio (AAPL, GOOGL, etc.), vous devez calculer la valeur actuelle, les gains/pertes potentiels, et d'autres métriques. Vous voulez des formules concises et rapides.

## 🎯 Concept : Les Fonctions Lambda appliquées à la finance
Les fonctions lambda sont parfaites pour les calculs financiers répétitifs. Au lieu d'écrire des fonctions complètes pour chaque calcul simple, vous créez des formules en une ligne. Avec votre portfolio concret, vous pouvez immédiatement tester sur de vraies données !

## 📚 Ressources utiles
- [Documentation Python sur les fonctions lambda](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Real Python - Guide complet sur les fonctions lambda](https://realpython.com/python-lambda/)
- [4 cas d'usage communs](https://datascientest.com/python-et-fonctions-lambda)

## 🎯 Objectif
**Créez des fonctions lambda pour tous les calculs financiers de base sur votre portfolio réel.**

## 📝 Exercice
Créez `portfolio_calculs.py` avec des lambdas essentielles :

### Fonctions lambda requises :
1. **`valeur_position`** - calcule la valeur d'achat d'une position : `quantity × purchase_price`
2. **`gain_absolu`** - calcule le gain en euros : `(prix_actuel - prix_achat) × quantity`
3. **`rendement_pourcent`** - calcule le rendement en % (gain ou perte): `((prix_actuel - prix_achat) / prix_achat) × 100`

### Fonctions lambda optionnelles :
4. **`poids_portfolio`** - pourcentage d'une position dans le portfolio total
5. **`valeur_actuelle`** - valeur actuelle : `quantity × prix_actuel`


## 🔍 Points d'attention
1. **Division par zéro** : Vérifiez que `purchase_price > 0`
2. **Précision** : Utilisez des floats pour les calculs monétaires
3. **Lisibilité** : Nommez vos lambdas de manière explicite

## 💡 Résultats de rendements attendus avec prix simulés
Utilisez portfolio_actual_prices_sample.csv pour récupérer des prix actuels simulés
- **AAPL** : 1500€ → +250€ (+16.7%)
- **GOOGL** : 12500€ → +500€ (+4.0%)  
- **TSLA** : 6400€ → -400€ (-6.25%)

## 🚀 Pour aller plus loin
- Créez une lambda pour calculer les dividendes annuels
- Ajoutez une lambda pour les frais de courtage (0.1% par transaction)

## 🔄 Impact sur la suite
Ces calculs lambda seront réutilisés dans TOUTES les étapes suivantes : map, portfolio class, API, graphiques ! Une lambda c'est souvent une des premières briques utilisée pour construire un programme en Python


# python_portfolio

Vous développez un tableau de bord pour analyser un portefeuille d'actions. 
L'objectif est simple : créer deux fonctionnalités principales pour les investisseurs : 
- La première permet de sélectionner une action avec des dates d'achat/vente pour calculer le gain/perte en euros. 
- La seconde est de pouvoir afficher un graphique montrant l'évolution de la valeur totale du portefeuille dans le temps.
Le système doit traiter des données historiques de bourse, valider les entrées utilisateur, et générer un graphique. Vous utiliserez des APIs financières pour récupérer les prix des actions en temps réel. Les calculs doivent être optimisés pour traiter plusieurs actions simultanément. L'interface web permettra aux utilisateurs de visualiser leur portefeuille facilement.

N'allez pas trop vite, suivez les étapes et réflechissez toujours à comment votre ancien code s'imbrique avec le nouveau  

Commandes :
- sudo apt install python3-venv
- python3 -m venv .venv
- source .venv/bin/activate
- pip install yfinance
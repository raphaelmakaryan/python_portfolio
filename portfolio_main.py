import csv
from collections import namedtuple

Position = namedtuple('Portfolio', "symbol quantity purchase_price purchase_date value_buy gain_now rendements")

"""
positions_problematiques = [
    Position('AAPL', 10, 10.0, '2023-01-15'),  # Prix d'achat = 0 !
    Position('NVDA', 5, 100.0, '2023-02-01'),  # Symbole inexistant
    Position('GOOGL', 10, 2500.0, '2023-03-01')  # Quantité négative !
]

positions_problematiques = [
Position('AAPL', 10, 0.0, '2023-01-15'),  
 Position('INVALID', 5, 100.0, '2023-02-01'), 
  Position('GOOGL', -10, 2500.0, '2023-03-01')  
]
"""


class Portfolio:
    def startup(self):
        data = Portfolio.lire_portfolio_csv("csv/portfolio_sample.csv")
        Portfolio.convertir_vers_positions(data)

    def lire_portfolio_csv(nom_du_fichier):
        with open(nom_du_fichier, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                data.append([row["symbol"], row["quantity"], row["purchase_price"], row["purchase_date"], 0, 0, 0])
            return data

    def data_actual_price():
        dataPrice = []
        valuePortfolio = Portfolio.lire_portfolio_csv("csv/portfolio_actual_prices_sample.csv")
        for price in valuePortfolio:
            dataPrice.append(float(price[2]))
        return dataPrice

    def convertir_vers_positions(portfolio_dict):
        data = []
        for i in portfolio_dict:
            data.append(Position(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        Portfolio.calculs(data)

    def calculer_valeurs_positions(quantity, purchase_price):
        valueCalcul = float(quantity) * float(purchase_price)
        Position.value_buy = valueCalcul
        return valueCalcul

    def calculer_gains_portfolio(positions, prix_actuels_dict):
        def calcul(position, prix_actuels):
            value = (prix_actuels - float(position.purchase_price)) * float(position.quantity)
            return value

        valueCalcul = calcul(positions)
        Position.gain_now = valueCalcul
        return list(map(calcul, positions, prix_actuels_dict))

    def calculer_rendements_portfolio(positions, prix_actuels_dict):
        def calcul(position, prix_actuels):
            value = round(((prix_actuels - float(position.purchase_price)) / float(position.purchase_price)) * 100, 1)
            return value

        valueCalcul = calcul(positions)
        Position.rendements = valueCalcul
        return list(map(calcul, positions, prix_actuels_dict))

    def calculs(dataValue):
        dataActualPrice = Portfolio.data_actual_price()
        for i in dataValue:
            Portfolio.calculer_valeurs_positions(i)
        """
            Portfolio.resultat(i.symbol, Portfolio.calculer_valeurs_positions(dataValue),
                               Portfolio.calculer_gains_portfolio(dataValue, dataActualPrice),
                               Portfolio.calculer_rendements_portfolio(dataValue, dataActualPrice))

        print("Valeurs d'achat :", Portfolio.calculer_valeurs_positions(dataValue))
        print("Gains actuels  :", Portfolio.calculer_gains_portfolio(dataValue, dataActualPrice))
        print("Rendements  :", Portfolio.calculer_rendements_portfolio(dataValue, dataActualPrice))
        """

    def resultat(entreprise, valeur, gain, randement):
        print(entreprise, ":", valeur, "€ ->", gain, "€ (+", randement, "%)")


Portfolio.startup(self=None)

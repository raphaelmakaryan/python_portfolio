import csv
from collections import namedtuple

Position = namedtuple('Portfolio', "symbol quantity purchase_price purchase_date value_buy gain_now rendements")


class ErreurDonneesPortfolio(Exception):
    def __init__(self, message):
        super().__init__(message)

    def validatePurchase(value):
        if value < 0:
            raise ErreurDonneesPortfolio("Vous avez un prix d'achat de 0 !")

    def validateSymbol(value):
        with open("csv/portfolio_sample.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            reponse = False
            for row in reader:
                data.append(row["symbol"])
            for verif in data:
                if (verif == value):
                    reponse = True
            if reponse == False:
                raise ErreurDonneesPortfolio("Vous avez un Symbole inexistant !")

    def validateQuantity(value):
        if value < 0:
            raise ErreurDonneesPortfolio("Vous avez une quantité négative !")


positions_problematiques = [
    Position('AAPL', 10, 0.0, '2023-01-15', 0, 0, 0),  # Prix d'achat = 0 !
    Position('INVALID', 5, 100.0, '2023-02-01', 0, 0, 0),  # Symbole inexistant
    Position('GOOGL', -10, 2500.0, '2023-03-01', 0, 0, 0)  # Quantité négative !
]
"""
positions_problematiques = [
    Position('AAPL', 10, 10.0, '2023-01-15'),  # Prix d'achat = 0 !
    Position('NVDA', 5, 100.0, '2023-02-01'),  # Symbole inexistant
    Position('GOOGL', 10, 2500.0, '2023-03-01')  # Quantité négative !
]
"""


class Portfolio:
    def startup(test):
        data = Portfolio.lire_portfolio_csv("csv/portfolio_sample.csv", test)
        Portfolio.convertir_vers_positions(data)

    def lire_portfolio_csv(nom_du_fichier, test):
        if test == False:
            with open(nom_du_fichier, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                data = []
                for row in reader:
                    ErreurDonneesPortfolio.validatePurchase(float(row["purchase_price"]))
                    ErreurDonneesPortfolio.validateSymbol(row["symbol"])
                    ErreurDonneesPortfolio.validateQuantity(float(row["quantity"]))
                    data.append([row["symbol"], row["quantity"], row["purchase_price"], row["purchase_date"], 0, 0, 0])
                return data
        else:
            data = []
            for row in positions_problematiques:
                ErreurDonneesPortfolio.validatePurchase(float(row.purchase_price))
                ErreurDonneesPortfolio.validateSymbol(row.symbol)
                ErreurDonneesPortfolio.validateQuantity(float(row.quantity))
                data.append([row.symbol, row.quantity, row.purchase_price, row.purchase_date, 0, 0, 0])
            return data

    def data_actual_price():
        dataPrice = []
        valuePortfolio = Portfolio.lire_portfolio_csv("csv/portfolio_actual_prices_sample.csv", False)
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

    def calculer_gains_portfolio(prix_actuels, purchase_price, quantity):
        valueCalcul = (prix_actuels - float(purchase_price)) * float(quantity)
        Position.value_buy = valueCalcul
        return valueCalcul

    def calculer_rendements_portfolio(prix_actuels, purchase_price):
        valueCalcul = round(((prix_actuels - float(purchase_price)) / float(purchase_price)) * 100, 1)
        Position.rendements = valueCalcul
        return valueCalcul

    def calculs(dataValue):
        dataActualPrice = Portfolio.data_actual_price()
        index = 0
        for i in dataValue:
            value = Portfolio.calculer_valeurs_positions(i.quantity, i.purchase_price)
            gain = Portfolio.calculer_gains_portfolio(dataActualPrice[index], i.purchase_price, i.quantity)
            rendement = Portfolio.calculer_rendements_portfolio(dataActualPrice[index], i.purchase_price)
            Portfolio.resultat(i.symbol, value, gain, rendement)
            index = index + 1

    def resultat(entreprise, valeur, gain, randement):
        print(entreprise, ":", valeur, "€ ->", gain, "€ (", randement, "%)")


Portfolio.startup(True)

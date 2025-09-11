import csv
import time
from collections import namedtuple
from main.portfolio_exceptions import *

Position = namedtuple('Portfolio', "symbol quantity purchase_price purchase_date value_buy gain_now rendements")

"""
positions_problematiques = [
    Position('AAPL', 10, 0.0, '2023-01-15', 0, 0, 0),  # Prix d'achat = 0 !
    Position('INVALID', 5, 100.0, '2023-02-01', 0, 0, 0),  # Symbole inexistant
    Position('GOOGL', -10, 2500.0, '2023-03-01', 0, 0, 0),  # Quantité négative !
    Position('TSLA', 10, 2500.0, '2023-0-01', 0, 0, 0)  # Date correspond pas
]
"""
positions_problematiques = [
    Position('AAPL', 10, 10.0, '2023-01-15', 0, 0, 0),  # Prix d'achat = 0 !
    Position('dsdsdsd', 5, 100.0, '2023-02-01', 0, 0, 0),  # Symbole inexistant
    Position('GOOGL', 10, 2500.0, '2023-03-01', 0, 0, 0),  # Quantité négative !
    Position('TSLA', 10, 2500.0, '2023-05-01', 0, 0, 0)  # Date correspond pas
]


def chronometre(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Durée : {end - start:.4f} secondes")
        return result

    return wrapper


class Portfolio:
    def __init__(self, positions):
        self.allPositions = positions
        Portfolio.convertir_vers_positions(self)

    def __len__(self):
        return len(self.allPositions)  # Retourne simplement la taille

    def charger_portfolio_securise(nom_du_fichier, test):
        if test == False:
            with open(nom_du_fichier, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                data = []
                for row in reader:
                    try:
                        check_purchase_price(float(row["purchase_price"]))
                        check_symbol(row["symbol"])
                        check_quantity(float(row["quantity"]))
                        check_date(row["purchase_date"])
                        data.append(
                            [row["symbol"], row["quantity"], row["purchase_price"], row["purchase_date"], 0, 0, 0])
                        pass
                    except ErreurDonneesPortfolio as e:
                        print(f"Erreur pour cet position : {row} car {e}")
                return data
        else:
            data = []
            for row in positions_problematiques:
                try:
                    check_purchase_price(row.purchase_price)
                    check_symbol(row.symbol)
                    check_quantity(row.quantity)
                    check_date(row.purchase_date)
                    data.append([row.symbol, row.quantity, row.purchase_price, row.purchase_date, 0, 0, 0])
                    pass
                except ErreurDonneesPortfolio as e:
                    print(f"Erreur pour cet position : {row} car {e}")
            return data

    def data_actual_price():
        dataPrice = []
        valuePortfolio = Portfolio.charger_portfolio_securise("csv/portfolio_actual_prices_sample.csv", False)
        for price in valuePortfolio:
            dataPrice.append(float(price[2]))
        return dataPrice

    def convertir_vers_positions(self):
        data = []
        dataActualPrice = Portfolio.data_actual_price()
        for i in self.allPositions:
            data.append(Position(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        Portfolio.calculer_gains_securise(data, dataActualPrice)

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

    @chronometre
    def calculer_gains_securise(positions, prix_actuels):
        index = 0
        for i in positions:
            value = Portfolio.calculer_valeurs_positions(i.quantity, i.purchase_price)
            gain = Portfolio.calculer_gains_portfolio(prix_actuels[index], i.purchase_price, i.quantity)
            rendement = Portfolio.calculer_rendements_portfolio(prix_actuels[index], i.purchase_price)
            Portfolio.resultat(i.symbol, value, gain, rendement)
            index = index + 1

    def resultat(entreprise, valeur, gain, randement):
        print(entreprise, ":", valeur, "€ ->", gain, "€ (", randement, "%)")

    def __str__(self):
        details = self.afficher_positions()
        return f"Portfolio avec {len(self)} positions :\n{details}"

    def obtenir_position(self, symbol):
        for pos in self.allPositions:
            if isinstance(pos, Position):
                if pos.symbol == symbol:
                    return pos
            else:
                if pos[0] == symbol:
                    return pos
        return None

    def afficher_positions(self):
        lignes = []
        for pos in self.allPositions:
            if isinstance(pos, Position):
                lignes.append(
                    f"{pos.symbol} | Qté: {pos.quantity} | Prix achat: {pos.purchase_price} | Date: {pos.purchase_date}")
            else:
                lignes.append(f"{pos[0]} | Qté: {pos[1]} | Prix achat: {pos[2]} | Date: {pos[3]}")
        return "\n".join(lignes)


portfolioData = Portfolio(Portfolio.charger_portfolio_securise("csv/portfolio_sample.csv", True))
"""
print(len(portfolioData))
print(portfolioData)
position = portfolioData.obtenir_position("AAPL")
print("Recherche AAPL :", position)
"""

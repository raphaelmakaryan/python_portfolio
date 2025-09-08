import json
import csv


def lire_portfolio_csv(nom_du_fichier):
    with open(nom_du_fichier, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append([row["symbol"], row["quantity"], row["purchase_price"]])
        return data


def data_actual_price():
    dataPrice = []
    valuePortfolio = lire_portfolio_csv("portfolio_actual_prices_sample.csv")
    for price in valuePortfolio:
        dataPrice.append(float(price[2]))
    return dataPrice


def data_clean_portfolio(data):
    dataActualPrice = data_actual_price()
    dataValue = []
    indexData = 0
    final = len(dataActualPrice)

    for valuePortfolio in data:
        if indexData < final:
            dataValue.append(
                [valuePortfolio[0], float(valuePortfolio[1]), float(valuePortfolio[2]), dataActualPrice[indexData]])
        indexData = indexData + 1

    print("Valeurs d'achat :", calculer_valeurs_positions(dataValue))
    print("Gains actuels  :", calculer_gains_portfolio(dataValue, dataActualPrice))
    print("Rendements  :", calculer_rendements_portfolio(dataValue, dataActualPrice))


def calculer_valeurs_positions(positions):
    def calcul(position):
        return position[1] * position[2]

    return list(map(calcul, positions))


def calculer_gains_portfolio(positions, prix_actuels_dict):
    def calcul(position, prix_actuels):
        value = (prix_actuels - position[2]) * position[1]
        return value

    return list(map(calcul, positions, prix_actuels_dict))


def calculer_rendements_portfolio(positions, prix_actuels_dict):
    def calcul(position, prix_actuels):
        value = round(((prix_actuels - position[2]) / position[2]) * 100, 1)
        return value

    return list(map(calcul, positions, prix_actuels_dict))


data_clean_portfolio(lire_portfolio_csv("portfolio_sample.csv"))
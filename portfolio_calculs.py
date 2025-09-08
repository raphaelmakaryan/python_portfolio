import json
import csv

valeur_position = lambda quantity, purchase_price: quantity * purchase_price
gain_absolu = lambda price_now, purchase_price, quantity: (price_now - purchase_price) * quantity
rendement_pourcent = lambda price_now, purchase_price: ((price_now - purchase_price) / purchase_price) * 100


# REfaire les boucles car une autre façon de le faire


def lire_portfolio_csv(nom_du_fichier):
    with open(nom_du_fichier, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append([row["symbol"], row["quantity"], row["purchase_price"]])
        return data


def lire_portfolio_json(nom_du_fichier):
    with open(nom_du_fichier, 'r') as file:
        data = json.load(file)
        return data


def chooseType(portfolio):
    if portfolio == "csv" or portfolio == "CSV":
        data_clean_portfolio(lire_portfolio_csv("portfolio_sample.csv"), portfolio)
    elif portfolio == "json" or portfolio == "JSON":
        data_clean_portfolio(lire_portfolio_json("portfolio_sample.json"), portfolio)


def data_actual_price():
    dataPrice = []
    valuePortfolio = lire_portfolio_csv("portfolio_actual_prices_sample.csv")
    for price in valuePortfolio:
        dataPrice.append(float(price[2]))
    return dataPrice


def data_clean_portfolio(data, type):
    if type == "csv" or type == "CSV":
        dataActualPrice = data_actual_price()
        dataValue = []
        indexData = 0
        indexCalcul = 0
        final = len(dataActualPrice)

        for valuePortfolio in data:
            if indexData < final:
                dataValue.append(
                    # 0 : entreprise | 1 : quantités | 2 : prix des quanités | 3 : prix actuel
                    [valuePortfolio[0], float(valuePortfolio[1]), float(valuePortfolio[2]), dataActualPrice[indexData]])
            indexData = indexData + 1

        for i in dataValue:
            resultat(i[0], valeur_position(i[1], i[2]), gain_absolu(dataActualPrice[indexCalcul], i[2], i[1]),
                     round(rendement_pourcent(dataActualPrice[indexCalcul], i[2]), 1))
            indexCalcul = indexCalcul + 1

    elif type == "json" or type == "JSON":
        dataActualPrice = data_actual_price()
        indexCalcul = 0

        for value in data['positions']:
            resultat(value["symbol"], valeur_position(value["quantity"], value["purchase_price"]),
                     gain_absolu(dataActualPrice[indexCalcul], value["purchase_price"], value["quantity"]),
                     round(rendement_pourcent(dataActualPrice[indexCalcul], value["purchase_price"]), 2))


def resultat(entreprise, valeur, gain, randement):
    print(entreprise, ":", valeur, "€ ->", gain, "€ (+", randement, "%)")


chooseType("csv")

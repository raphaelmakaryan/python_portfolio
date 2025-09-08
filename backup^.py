import json
import csv

valeur_position = lambda quantity, purchase_price: quantity * purchase_price
gain_absolu = lambda quantity, purchase_price, price_now: (price_now - purchase_price) * quantity
rendement_pourcent = lambda quantity, purchase_price, price_now: ((price_now - purchase_price) / purchase_price) * 100


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
    index = 0
    dataPrice = []
    valuePortfolio = lire_portfolio_csv("portfolio_actual_prices_sample.csv")
    for price in valuePortfolio:
        if index != 0:
            dataPrice.append(float(price[2]))
        index = index + 1
    return dataPrice


def data_clean_portfolio(data, type):
    if type == "csv" or type == "CSV":
        dataActualPrice = data_actual_price()
        dataValue = []
        index = 0
        final = len(dataActualPrice)

        for valuePortfolio in data:
            if index < final:
                dataValue.append(
                    [valuePortfolio[0], float(valuePrice[2]), float(valuePortfolio[2], dataActualPrice[index])])
            print(dataValue)
            index = index + 1

        for i in dataValue:
            vPosition = valeur_position(i[1], i[2])
            resultat(i[0], vPosition, gain_absolu(i[1], i[2], vPosition), rendement_pourcent(i[1], i[2], vPosition))

    elif type == "json" or type == "JSON":
        for value in data['positions']:
            vPosition = valeur_position(value["quantity"], value["purchase_price"])
            resultat(value["symbol"], vPosition, gain_absolu(value["quantity"], value["purchase_price"], vPosition),
                     rendement_pourcent(value["quantity"], value["purchase_price"], vPosition))


def resultat(entreprise, valeur, gain, randement):
    print(entreprise, ":", valeur, "€ ->", gain, "€ (+", randement, "%)")


chooseType("csv")

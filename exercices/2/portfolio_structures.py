import json
import csv
from collections import namedtuple

Position = namedtuple('Portfolio', "symbol quantity purchase_price purchase_date type")


def lire_portfolio_csv(nom_du_fichier):
    with open(nom_du_fichier, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append([row["symbol"], row["quantity"], row["purchase_price"], row["purchase_date"]])
        return data


def lire_portfolio_json(nom_du_fichier):
    with open(nom_du_fichier, 'r') as file:
        data = json.load(file)
        return data


class Portfolio:
    def portfolio_type(typeData):
        if typeData == "csv" or typeData == "CSV":
            dataCSV = lire_portfolio_csv("../../csv/portfolio_sample.csv")
            dataArray = []
            for value in dataCSV:
                dataArray.append([value[0], value[1], value[2], value[3]])
            return dataArray

        elif typeData == "json" or typeData == "JSON":
            dataJSON = lire_portfolio_json("portfolio_sample.json")
            dataArray = []
            for value in dataJSON['positions']:
                dataArray.append([value["symbol"], value["quantity"], value["purchase_price"], value["purchase_date"]])
            return dataArray

    def convertir_vers_positions(portfolio_dict):
        data = []
        for i in portfolio_dict:
            data.append(Position(i[0], i[1], i[2], i[3], "purchase"))
        return data

    def afficher_positions(positions):
        for i in positions:
            print("Entreprise :", i.symbol, "| Quantité :", i.quantity, " | Prix d'achat : ", i.purchase_price,
                  "| Date d'achat :", i.purchase_date, "| Type : ", i.type)


dataPortfolio = Portfolio.portfolio_type("csv")
dictPortfolio = Portfolio.convertir_vers_positions(dataPortfolio)
displayPortfolio = Portfolio.afficher_positions(dictPortfolio)

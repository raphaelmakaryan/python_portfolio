import json
import csv

def lire_portfolio_csv(nom_du_fichier):
    with open(nom_du_fichier, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append([row["symbol"], row["quantity"], row["purchase_price"], row["purchase_date"]])
        return data


def rendu_propre_csv(data):
    index = 0
    for value in data:
        if index != 0:
            print("L'entreprise", value[0], "à", value[1], "actions au prix de", value[2], "€ acheter le", value[3])
        index = index + 1


def lire_portfolio_json(nom_du_fichier):
    with open(nom_du_fichier, 'r') as file:
        data = json.load(file)
        return data


def rendu_propre_json(data):
    for value in data['positions']:
        print("L'entreprise", value["symbol"], "à", value["quantity"], "actions au prix de", value["purchase_price"],
              "€ acheter le", value["purchase_date"])


def afficher_portfolio(portfolio):
    if portfolio == "csv" or portfolio == "CSV":
        rendu_propre_csv(lire_portfolio_csv("portfolio_sample.csv"))
    elif portfolio == "json" or portfolio == "JSON":
        rendu_propre_json(lire_portfolio_json("portfolio_sample.json"))


afficher_portfolio("csv")
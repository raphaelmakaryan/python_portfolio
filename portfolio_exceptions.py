from collections import namedtuple
import csv

Position = namedtuple('Portfolio', "symbol quantity purchase_price purchase_date")


class ErreurDonneesPortfolio(Exception):
    def __init__(self, message):
        super().__init__(message)

    def validatePurchase(value):
        if value <= 0:
            raise ErreurDonneesPortfolio("Vous avez un 0 !")

    def validateSymbol(value):
        with open("portfolio_sample.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            reponse = False
            for row in reader:
                data.append(row["symbol"])
            print(data)
            for verif in data:
                if (verif != value):
                    reponse = True
                reponse = float


def charger_portfolio_securise(test, nom_du_fichier):
    if test is False:
        with open(nom_du_fichier, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                try:
                    ErreurDonneesPortfolio.validatePurchase(float(row["quantity"]))
                    ErreurDonneesPortfolio.validateSymbol(row["symbol"])
                    data.append([row["symbol"], row["quantity"], row["purchase_price"], row["purchase_date"]])
                except ErreurDonneesPortfolio:
                    pass

            return data

    elif test is True:
        return []


def data_actual_price():
    dataPrice = []
    valuePortfolio = charger_portfolio_securise(False, "portfolio_actual_prices_sample.csv")
    for price in valuePortfolio:
        dataPrice.append(float(price[2]))
    return dataPrice


positions_problematiques = [
    Position('AAPL', 10, 0.0, '2023-01-15'),  # Prix d'achat = 0 !
    Position('INVALID', 5, 100.0, '2023-02-01'),  # Symbole inexistant
    Position('GOOGL', -10, 2500.0, '2023-03-01')  # Quantité négative !
]


class Portfolio:
    def portfolio(self):
        dataCSV = charger_portfolio_securise(False, "portfolio_sample.csv")
        dataArray = []
        for value in dataCSV:
            dataArray.append([value[0], value[1], value[2], value[3]])
        Portfolio.convertir_vers_positions(dataArray)

    def convertir_vers_positions(portfolio_dict):
        data = []
        for i in portfolio_dict:
            data.append(Position(i[0], i[1], i[2], i[3]))

        Portfolio.afficher_positions(data)

    def afficher_positions(positions):
        for i in positions:
            return
            # print("Entreprise :", i.symbol, "| Quantité :", i.quantity, " | Prix d'achat : ", i.purchase_price,  "| Date d'achat :", i.purchase_date)


Portfolio.portfolio(self=None)

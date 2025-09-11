import re
from main.portfolio_verification import *


class ErreurDonneesPortfolio(Exception):
    def __init__(self, message):
        super().__init__(message)


class PurchasePriceError(Exception):
    def __init__(self, message):
        super().__init__(message)


def check_purchase_price(value):
    if value == 0:
        raise PurchasePriceError("vous avez un prix d'achat de 0 !")
    elif value < 0:
        raise PurchasePriceError("vous avez un prix d'achat négative !")


class SymbolNotFoundError(ErreurDonneesPortfolio):
    def __init__(self, message):
        super().__init__(message)


def check_symbol(value):
    verification = valider_portfolio_complet(value)
    if verification[0] == True:
        symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA", "AMZN", "META"]
        if verification[1] not in symbols:
            raise SymbolNotFoundError("vous avez un symbole inexistant !")
    else:
        raise SymbolNotFoundError("vous avez un symbole qui ne respecte pas notre pattern !")


class QuantityError(ErreurDonneesPortfolio):
    def __init__(self, message):
        super().__init__(message)


def check_quantity(value):
    if value < 0:
        raise QuantityError("vous avez une quantité négative !")
    elif value == 0:
        raise QuantityError("vous avez une quantité de 0 !")


class DateError(ErreurDonneesPortfolio):
    def __init__(self, message):
        super().__init__(message)


def check_date(date_str):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date_str):
        raise DateError("La date que vous avez indiquée ne correspond pas au pattern : YYYY-MM-DD !")

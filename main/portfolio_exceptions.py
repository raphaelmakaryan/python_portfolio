import re

class ErreurDonneesPortfolio(Exception):
    def __init__(self, message):
        super().__init__(message)


class PurchasePriceError(Exception):
    def __init__(self, message):
        super().__init__(message)


def check_purchase_price(value):
    if value == 0:
        raise PurchasePriceError("Vous avez un prix d'achat de 0 !")
    elif value < 0:
        raise PurchasePriceError("Vous avez un prix d'achat négative !")


class SymbolNotFoundError(ErreurDonneesPortfolio):
    def __init__(self, message):
        super().__init__(message)


def check_symbol(value):
    symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA", "AMZN", "META"]
    if value not in symbols:
        raise SymbolNotFoundError("Vous avez un symbole inexistant !")


class QuantityError(ErreurDonneesPortfolio):
    def __init__(self, message):
        super().__init__(message)


def check_quantity(value):
    if value < 0:
        raise QuantityError("Vous avez une quantité négative !")
    elif value == 0:
        raise QuantityError("Vous avez une quantité de 0 !")


class DateError(ErreurDonneesPortfolio):
    def __init__(self, message):
        super().__init__(message)


def check_date(date_str):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date_str):
        raise DateError("La date que vous avez indiquée ne correspond pas au pattern : YYYY-MM-DD !")

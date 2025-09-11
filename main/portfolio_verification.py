import re


def verifier_string(symbole):
    pattern = re.compile("^[a-zA-Z]+$")
    if not re.match(pattern, symbole):
        return False
    else:
        return True


def valider_symbole_action(symbole):
    newValue = nettoyer_symbole(symbole)
    ifString = verifier_string(newValue[1])
    if ifString:
        pattern = r'^[A-Z]{1,5}$'
        if not re.match(pattern, newValue[1]):
            return [False, newValue[1]]
        else:
            return [True, newValue[1]]
    else:
        return [False, newValue[1]]


def valider_portfolio_complet(positions):
    valide, symbole_nettoye = valider_symbole_action(positions)
    return [valide, symbole_nettoye]


def nettoyer_symbole(symbole_brut):
    upper = symbole_brut.upper()
    deleteSpace = upper.replace(" ", "")
    if upper and deleteSpace:
        return [True, deleteSpace]
    else:
        return [False, symbole_brut]


def get_essentials()->list:
    """
    Returns a list of essential items for the user to pack for a hurricane from the file "essetial_items.txt"
    """
    with open ("essetial_items.txt", "r") as file:
        essentials=[line.strip() for line in file]
        return essentials

def country_options()->list:
    """
    Returns a list of supported countries
    """
    options = [ 
        "Anguilla", 
        "Antigua and Barbuda", 
        "Bahamas", 
        "Barbados", 
        "Belize", 
        "Bermuda", 
        "Bonaire",
        "British Virgin Islands",
        "Cayman Islands",
        "Cuba",
        "Curacao",
        "Dominica",
        "Grenada",
        "Guadeloupe",
        "Jamaica",
        "Martinique",
        "Montserrat",
        "Puerto Rico",
        "Saba",
        "Saint Barthélemy",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Martin",
        "Saint Vincent and the Grenadines",
        "Eustatius",
        "Trinidad and Tobago",
        "Turks and Caicos Islands"
    ]
    return options
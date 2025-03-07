
def get_essentials()->list:
    """
    Returns a list of essential items for the user to pack for a hurricane from the file "essetial_items.txt"
    """
    with open ("essetial_items.txt", "r") as file:
        essentials=[line.strip() for line in file]
        print(essentials)
        return essentials


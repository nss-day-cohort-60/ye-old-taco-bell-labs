PRODUCTS = [
    {
        "id": 1,
        "name": "Loco Gorpeno Supreme",
        "type_id": 1,
        "date_created": "01/11/2023",
        "suggested_price": 8.49
    },
    {
        "id": 2,
        "name": "Loaded-Mini Taizo Crunch",
        "type_id": 1,
        "date_created": "01/11/2023",
        "suggested_price": 1.49
    },
    {
        "id": 3,
        "name": "Triple-Layer Beefaloco Supreme Bowl",
        "type_id": 2,
        "date_created": "01/11/2023",
        "suggested_price": 19.99
    },
    {
        "id": 4,
        "name": "Bean Crunchobowl-Choritadilla",
        "type_id": 2,
        "date_created": "01/10/2023",
        "suggested_price": 0.50
    }
]

def get_all_products():
    """Get entire list of products

    Returns:
        list: The list of product dictionaries
    """
    return PRODUCTS

def get_single_product(id):
    """Get a single product from the list of dictionaries

    Args:
        id (int): Primary key of requested product

    Returns:
        dictionary: Found dictionary in list
    """
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product

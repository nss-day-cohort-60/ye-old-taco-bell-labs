import random

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
        "id": 5,
        "name": "Triple-Layer Beefaloco Supreme Bowl",
        "type_id": 2,
        "date_created": "01/11/2023",
        "suggested_price": 19.99
    },
    {
        "id": 8,
        "name": "Bean Crunchobowl-Choritadilla",
        "type_id": 2,
        "date_created": "01/10/2023",
        "suggested_price": 0.50
    },
    {
        "id": 12,
        "name": "Fiesta Yumtada Supreme Taco",
        "type_id": 3,
        "date_created": "01/13/2023",
        "suggested_price": 5.50
    }
]

def remove_product(id):
    """Remove a dictionary from the product list

    Args:
        id (int): Primary key of item to delete

    Returns:
        bool: Whether the product was found an deleted
    """
    index_to_remove = -1

    for index, product in enumerate(PRODUCTS):
        if product['id'] == id:
            index_to_remove = index

    if index_to_remove > -1:
        del PRODUCTS[index_to_remove]
        return True
    else:
        return False

def get_product_id():
    """Get a random primary key of a dictionary in the product list

    Returns:
        int: primary key
    """
    random_product = random.choice(PRODUCTS)
    return random_product['id']


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

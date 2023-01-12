PRODUCT_TYPES = [
    {"id": 1,
    "description": "burrito"

    },
    {
        "id": 2,
        "description": "bowl"
    },
    {
        "id": 3,
        "description": "taco"
    },
    {
        "id": 4,
        "description": "chalupa"
    }
]

def get_all_product_types():
    """Get entire list of products

    Returns:
        list: The list of product dictionaries
    """
    return PRODUCT_TYPES
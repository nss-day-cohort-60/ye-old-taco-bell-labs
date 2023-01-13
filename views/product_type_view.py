PRODUCT_TYPES = [
    {
        "id": 1,
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
    """Get entire list of product types

    Returns:
        list: The list of product type dictionaries
    """
    return PRODUCT_TYPES

def create_product_type(product_type):
    """Create a product type

    Returns:
        the new product type
    """
    max_id = PRODUCT_TYPES[-1]["id"]
    new_id = max_id + 1
    product_type["id"] = new_id
    PRODUCT_TYPES.append(product_type)
    return product_type
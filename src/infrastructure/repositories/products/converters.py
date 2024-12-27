
from src.domain.products.entity import Product


def convert_product_entity_to_document(product: Product) -> dict:
    return {
        "oid": product.oid,
        "name": product.name,
        "price": str(product.price),
        "category_id": product.category_id,
    }

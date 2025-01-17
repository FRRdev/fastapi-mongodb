from collections.abc import Mapping
from decimal import Decimal
from typing import Any

from src.domain.categories.entity import Category
from src.domain.products.entity import Product


def convert_product_entity_to_document(product: Product) -> dict:
    return {
        "oid": product.oid,
        "name": product.name,
        "slug": product.slug,
        "price": str(product.price),
        "category_id": product.category_id,
    }


def convert_product_document_to_entity(
    product_document: Mapping[str, Any],
) -> Product:
    return Product(
        oid=product_document["oid"],
        name=product_document["name"],
        price=Decimal(product_document["price"]),
        slug=product_document.get("slug"),
        category=Category(
            oid=product_document["category"]["oid"],
            name=product_document["category"]["name"],
            order=product_document["category"]["order"],
        ),
    )


def convert_sample_product_document_to_entity(
    product_document: Mapping[str, Any],
) -> Product:
    return Product(
        oid=product_document["oid"],
        name=product_document["name"],
        price=product_document["price"],
        slug=product_document["slug"],
    )

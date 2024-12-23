from collections.abc import Mapping
from typing import Any

from src.domain.categories.entity import Category


def convert_category_entity_to_document(category: Category) -> dict:
    return {
        "oid": category.oid,
        "name": category.name,
        "order": category.order,
    }


def convert_category_document_to_entity(
        category_document: Mapping[str, Any],
) -> Category:
    return Category(
        oid=category_document["oid"],
        name=category_document["name"],
        order=category_document["order"],
    )


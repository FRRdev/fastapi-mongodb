from src.domain.categories.entity import Category


def convert_category_entity_to_document(category: Category) -> dict:
    return {
        "oid": category.oid,
        "name": category.name,
        "order": category.order,
    }

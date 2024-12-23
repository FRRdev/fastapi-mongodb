
from pydantic import BaseModel

from src.domain.categories.entity import Category


class CategoryOutSchema(BaseModel):
    oid: str
    name: str
    order: int

    @classmethod
    def from_entity(cls, category: Category) -> "CategoryOutSchema":
        return CategoryOutSchema(
            oid=category.oid,
            name=category.name,
            order=category.order,
        )


class CategoryListOutSchema(BaseModel):
    count: int
    next_page: bool
    items: list[CategoryOutSchema]

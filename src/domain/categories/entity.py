from dataclasses import dataclass

from src.utils.entity import BaseEntity


@dataclass
class Category(BaseEntity):
    name: str
    order: int
    product_count: int | None = None

from dataclasses import dataclass

from fastapi import Query


@dataclass
class CategoryQuery:
    offset: int = Query(0, ge=0, description="Сдвиг")
    limit: int = Query(8, le=40, ge=0, description="Кол-во записей")

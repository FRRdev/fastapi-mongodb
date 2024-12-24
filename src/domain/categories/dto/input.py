from pydantic import BaseModel


class CategoryInSchema(BaseModel):
    name: str
    order: int

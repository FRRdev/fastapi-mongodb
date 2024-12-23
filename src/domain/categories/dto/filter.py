from pydantic import BaseModel


class CategoryFilterSchema(BaseModel):
    offset: int
    limit: int

    @property
    def pagination(self) -> tuple[int, int]:
        return self.offset, self.limit

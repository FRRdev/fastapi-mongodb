from pydantic import BaseModel


class UserInSchema(BaseModel):
    email: str

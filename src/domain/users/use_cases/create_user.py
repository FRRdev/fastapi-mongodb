from attr import define

from src.domain.users.dto.input import UserInSchema
from src.domain.users.entity import User
from src.domain.users.exceptions import (
    UserExistsException,
    UserExistsRepositoryException,
)
from src.domain.users.interfaces import IUserRepo


@define
class CreateUser:
    user_repo: IUserRepo

    async def __call__(self, schema: UserInSchema) -> User:
        user = User(email=schema.email)
        try:
            await self.user_repo.add_user(user)
        except UserExistsRepositoryException as err:
            raise UserExistsException(schema.email) from err

        return user

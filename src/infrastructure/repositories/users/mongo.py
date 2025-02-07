from collections.abc import AsyncGenerator
from dataclasses import dataclass

from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

from src.domain.users.entity import User
from src.domain.users.exceptions import UserExistsRepositoryException
from src.infrastructure.repositories.base import BaseMongoDBRepository
from src.infrastructure.repositories.users.converters import (
    convert_user_entity_to_document,
)


@dataclass
class MongoDBUsersRepository(BaseMongoDBRepository):
    async def add_user(self, user: User) -> None:
        try:
            await self._collection.insert_one(convert_user_entity_to_document(user))
        except DuplicateKeyError as err:
            raise UserExistsRepositoryException from err

    async def create_unique_email_constraint(self) -> None:
        await self._collection.create_index([("email", ASCENDING)], unique=True)

    async def get_user_ids(
        self,
    ) -> AsyncGenerator[str, None]:
        async for user_document in self._collection.find():
            yield user_document["oid"]

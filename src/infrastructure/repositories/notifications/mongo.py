from dataclasses import dataclass

from src.domain.notifications.entity import Notification, UserNotification
from src.infrastructure.repositories.base import BaseMongoDBRepository
from src.infrastructure.repositories.notifications.converters import (
    convert_notification_entity_to_document,
    convert_user_notification_entity_to_document,
)


@dataclass
class MongoDBNotificationsRepository(BaseMongoDBRepository):
    async def add_notification(self, notification: Notification) -> None:
        await self._collection.insert_one(
            convert_notification_entity_to_document(notification),
        )


@dataclass
class MongoDBUserNotificationsRepository(BaseMongoDBRepository):
    async def add_user_notifications_batch(
        self,
        user_notifications: list[UserNotification],
    ) -> None:
        user_notification_documents = [
            convert_user_notification_entity_to_document(user_notification)
            for user_notification in user_notifications
        ]
        await self._collection.insert_many(user_notification_documents)

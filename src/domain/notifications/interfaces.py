from typing import Protocol

from src.domain.notifications.entity import Notification, UserNotification


class IConsumeAndCreateNotification(Protocol):
    async def __call__(self) -> None: ...


class INotificationRepo(Protocol):
    async def add_notification(self, notification: Notification) -> None: ...


class IUserNotificationRepo(Protocol):
    async def add_user_notifications_batch(
        self,
        user_notifications: list[UserNotification],
    ) -> None: ...

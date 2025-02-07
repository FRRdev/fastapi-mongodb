from attr import define

from src.domain.notifications.dto.input import (
    BaseNotificationInSchema,
    NotificationManager,
)
from src.domain.notifications.entity import Notification, UserNotification
from src.domain.notifications.enums import NotificationType
from src.domain.notifications.interfaces import INotificationRepo, IUserNotificationRepo
from src.domain.products.interfaces import IMessageBroker
from src.domain.users.interfaces import IUserRepo


@define
class ConsumeAndCreateNotifications:
    notification_repo: INotificationRepo
    user_notification_repo: IUserNotificationRepo
    user_repo: IUserRepo
    message_broker: IMessageBroker

    async def __call__(self):
        async for msg in self.message_broker.start_consuming("products"):  # type: ignore[attr-defined]
            notification_schema = NotificationManager(**msg).root
            message_text = self._get_notification_message(notification_schema)
            notification = Notification(
                created_at=notification_schema.created_at,
                text=message_text,
            )
            await self.notification_repo.add_notification(notification)
            user_notifications = [
                UserNotification(user_id=user_id, notification_id=notification.oid)
                async for user_id in self.user_repo.get_user_ids()  # type: ignore[attr-defined]
            ]
            await self.user_notification_repo.add_user_notifications_batch(
                user_notifications,
            )

    def _get_notification_message(
        self,
        notification_schema: BaseNotificationInSchema,
    ) -> str:
        def generate_new_product_notification_text(
            notification: BaseNotificationInSchema,
        ) -> str:
            return f"В продаже новый продукт: {notification.product_name}"  # type: ignore[attr-defined]

        text_map_generators = {
            NotificationType.create_product: generate_new_product_notification_text,
        }

        return text_map_generators[notification_schema.notification_type](  # type: ignore[attr-defined]
            notification_schema,
        )

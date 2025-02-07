from src.domain.notifications.entity import Notification, UserNotification


def convert_notification_entity_to_document(notification: Notification) -> dict:
    return {
        "oid": notification.oid,
        "text": notification.text,
        "created_at": notification.created_at,
    }


def convert_user_notification_entity_to_document(
    user_notification: UserNotification,
) -> dict:
    return {
        "oid": user_notification.oid,
        "user_id": user_notification.user_id,
        "notification_id": user_notification.notification_id,
        "read": user_notification.read,
    }

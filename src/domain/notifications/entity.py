from dataclasses import dataclass
from datetime import datetime

from src.utils.entity import BaseEntity


@dataclass
class Notification(BaseEntity):
    text: str
    created_at: datetime


@dataclass
class UserNotification(BaseEntity):
    user_id: str
    notification_id: str
    read: bool = False

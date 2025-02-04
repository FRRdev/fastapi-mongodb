from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, RootModel

from src.domain.notifications.enums import NotificationType


class BaseNotificationInSchema(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)


class CreateProductNotificationInSchema(BaseNotificationInSchema):
    product_name: str
    notification_type: Literal[NotificationType.create_product]


class NotificationManager(RootModel):
    root: CreateProductNotificationInSchema = Field(discriminator="notification_type")

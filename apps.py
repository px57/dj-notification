"""
This file represents the configuration of the notification app.
"""

from django.apps import AppConfig


class NotificationConfig(AppConfig):
    """
    This class represents the configuration of the notification app.
    """

    """
    The default auto field.
    """
    default_auto_field = "django.db.models.BigAutoField"

    """
    The name of the app.
    """
    name = "notification"

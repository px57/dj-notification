"""
This module contains the Notification model.
"""

from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from notification.rules.stack import NOTIFICATION_RULESTACK

class Notification(BaseMetadataModel):
    """
    This class represents a notification.
    """

    sender = models.ForeignKey(
        'profiles.Profile', 
        on_delete=models.CASCADE, 
        related_name='sent_notifications',
        null=True,
        blank=True
    )

    receiver = models.ForeignKey(
        'profiles.Profile', 
        on_delete=models.CASCADE, 
        related_name='received_notifications',
    )

    interface = models.CharField(
        max_length=255, 
        choices=NOTIFICATION_RULESTACK.models_choices()
    )    

    expiration = models.DateTimeField(
        null=True, 
        blank=True
    )

    params = models.JSONField(
        null=True, 
        blank=True,
        default=dict
    )

    def __str__(self):
        """
        Returns the string representation of the notification.
        """
        return ''

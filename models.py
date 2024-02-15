"""
This module contains the Notification model.
"""

from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from notification.rules.stack import NOTIFICATION_RULESTACK
from django.forms.models import model_to_dict
from kernel.models.serialize import serializer__serialize__, serializer__init__
from kernel.i18n.models import translateDBQuerySet, translateDBObject

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
    

class NotificationMessageTranslate(BaseMetadataModel):
    """
        @description:
    """
    language = models.CharField(
        'language',
        max_length=255,
        default='fr',
        choices=(
            ('fr', 'fr'),
        ),
    )
    name = models.CharField(
        'name',
        max_length=255,
        blank=True,
        null=True,
    )

    description = models.TextField(
        'description',
        blank=True,
        null=True,
    )

    translateObject = models.ForeignKey(
        'notification.NotificationMessage',
        on_delete=models.CASCADE,
        related_name='translates',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.language
    
    @serializer__serialize__
    def serialize(self, request):
        """
            @description: 
        """
        serialize = model_to_dict(self)
        return serialize

class NotificationMessage(BaseMetadataModel):
    """
    This class represents a notification message.
    """

    interface = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        choices=NOTIFICATION_RULESTACK.models_choices()
    )

    object = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
    )

    message = models.TextField(
        null=True, 
        blank=True,
        unique=True,
    )

    @serializer__serialize__
    def serialize(self, request):
        """
        Returns the serialized object.
        """
        serialize = model_to_dict(self)
        return serialize
    
    def __str__(self):
        """
        Returns the string representation of the notification message.
        """
        return self.message

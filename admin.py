from django.contrib import admin
from notification.models import Notification
from notification.models import NotificationMessage

# Register your models here.
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'interface', 
    )

@admin.register(NotificationMessage)
class NotificationMessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'interface',
        'message',
    )
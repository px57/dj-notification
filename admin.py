from django.contrib import admin
from notification.models import NotificationSended
from notification.models import NotificationTemplate
from notification.models import NotificationUnsubscribe

# Register your models here.
@admin.register(NotificationSended)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'interface', 
    )

@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'interface',
        'message',
    )

@admin.register(NotificationUnsubscribe)
class NotificationUnsubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'interface',
    )
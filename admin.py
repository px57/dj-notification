from django.contrib import admin
from notification.models import NotificationSended
from notification.models import NotificationTemplate
from notification.models import NotificationUnsubscribe
from notification.models import NotificationTemplateTranslate
from django.forms import ModelForm
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(NotificationSended)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'interface', 
    )

class NotificationTranslateInline(admin.TabularInline):
    """
        @description: NotificationTranslateInline
    """

    model = NotificationTemplateTranslate
    extra = 0

    fields = [
        'language',
        'object',
        'message',
    ]
    formfield_overrides = {

    }
 
    
@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'interface',
        'message',
    )
    inlines = [NotificationTranslateInline]

@admin.register(NotificationUnsubscribe)
class NotificationUnsubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'interface',
    )
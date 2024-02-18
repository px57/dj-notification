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

class NotificationTemplateAdmin(admin.ModelAdmin):
    """
        @description: JobCategoryInline
    """

    model = NotificationTemplateTranslate
    extra = 0

    fields = [
        'language', 
        'object', 
        'message']
    readonly_fields = ['link']
    formfield_overrides = {

    }

    def link(self, obj):
        if obj.pk is None:
            return ''
        return mark_safe(
            '<a href="/admin/jobs/job/' + str(obj.pk) + '/change/" target="_blank">OPEN</a>'
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
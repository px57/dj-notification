# Generated by Django 4.2 on 2024-02-18 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NotificationMessage',
            new_name='NotificationTemplate',
        ),
        migrations.RenameModel(
            old_name='NotificationMessageTranslate',
            new_name='NotificationTemplateTranslate',
        ),
    ]
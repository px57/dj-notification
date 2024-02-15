# Generated by Django 4.2 on 2024-02-15 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notificationmessage_alter_notification_interface'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationmessage',
            old_name='key',
            new_name='interface',
        ),
        migrations.AddField(
            model_name='notificationmessage',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
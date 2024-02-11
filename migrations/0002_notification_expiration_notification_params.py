# Generated by Django 4.2 on 2024-02-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='params',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
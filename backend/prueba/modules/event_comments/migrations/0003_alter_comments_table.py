# Generated by Django 5.1.5 on 2025-01-20 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_comments', '0002_comments_delete_events'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comments',
            table='event_comments',
        ),
    ]

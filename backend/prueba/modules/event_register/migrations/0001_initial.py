# Generated by Django 5.1.5 on 2025-01-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('imagen', models.ImageField(upload_to='eventos/imagenes/')),
                ('capacity', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('ubication', models.CharField(max_length=255)),
            ],
        ),
    ]

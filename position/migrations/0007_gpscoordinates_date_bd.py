# Generated by Django 4.2.2 on 2024-06-20 16:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0006_gpsmodule_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpscoordinates',
            name='date_bd',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
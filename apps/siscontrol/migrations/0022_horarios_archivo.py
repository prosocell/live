# Generated by Django 2.1.4 on 2019-01-11 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siscontrol', '0021_auto_20190110_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='horarios',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='comalu', verbose_name='Archivo'),
        ),
    ]

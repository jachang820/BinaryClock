# Generated by Django 2.0.1 on 2018-01-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binaryclock', '0002_auto_20180114_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_zone',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='end.timeZone'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_zone',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='start.timeZone'),
        ),
    ]

# Generated by Django 3.2.15 on 2023-01-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientadress',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Город'),
        ),
    ]

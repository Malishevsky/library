# Generated by Django 3.2.15 on 2023-01-06 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_bookauthorsfoto_author'),
        ('client', '0002_clientadress_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownedbook',
            name='owneded_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book', verbose_name='Книга'),
        ),
    ]
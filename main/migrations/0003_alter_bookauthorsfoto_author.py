# Generated by Django 3.2.15 on 2023-01-06 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_book_authors_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthorsfoto',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.authors', verbose_name='Автор'),
        ),
    ]

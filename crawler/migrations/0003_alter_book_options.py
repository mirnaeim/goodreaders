# Generated by Django 4.2 on 2024-02-15 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_remove_book_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('rating',), 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]

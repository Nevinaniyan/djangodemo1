# Generated by Django 5.0.3 on 2024-03-23 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='categories',
            new_name='category',
        ),
    ]

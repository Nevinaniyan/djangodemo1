# Generated by Django 5.0.3 on 2024-03-23 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_category_categories_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='name',
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-29 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200326_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyapp', '0005_remove_product_discount_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

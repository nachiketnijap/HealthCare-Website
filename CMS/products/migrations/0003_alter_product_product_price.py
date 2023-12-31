# Generated by Django 4.2.2 on 2023-07-27 07:08

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_entered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.PositiveIntegerField(validators=[products.models.positive_validator]),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_cart_to_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cart_to_product',
        ),
        migrations.AddField(
            model_name='product',
            name='cart_to_product',
            field=models.ManyToManyField(blank=True, null=True, to='shop.cartitem'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_same_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='same_product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='same_item',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-17 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerApp', '0007_product_product_discription'),
        ('UserApp', '0003_wishlistitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistitem',
            name='image_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SellerApp.image'),
        ),
    ]

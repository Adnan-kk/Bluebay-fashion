# Generated by Django 5.0.3 on 2024-05-22 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SellerApp', '0007_product_product_discription'),
        ('UserApp', '0005_remove_wishlistitem_image_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Cart_Item',
        ),
    ]
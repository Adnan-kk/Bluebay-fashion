from django.db import models
from SellerApp.models import *

# Create your models here.

class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,default="active")

    class Meta:
        db_table ='user_table'

    def __str__(self):
        return self.user_name

class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    house_name = models.CharField(max_length=200)

    class Meta:
        db_table='user_address_table'


class Order(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=100)
    address_id = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default="pending")

    class Meta:
        db_table = 'order_table'

class Cart_Item(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=100)
    status = models.CharField(max_length=200,default='pending')

    class Meta:
        db_table = 'cart_table'

class Contact(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    comments = models.TextField(max_length=500)

    class Meta:
        db_table = 'contact_table'


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    Feedback = models.CharField(max_length=500)
    user_id = models.ForeignKey(UserDetails,on_delete=models.CASCADE)

    class Meta:
        db_table = 'feedback_table'

class WishlistItem(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wishlist_table'
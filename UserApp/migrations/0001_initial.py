# Generated by Django 5.0.3 on 2024-04-15 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SellerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='active', max_length=100)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('Feedback', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user')),
            ],
            options={
                'db_table': 'feedback_table',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('comments', models.TextField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user')),
            ],
            options={
                'db_table': 'contact_table',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=100)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user')),
            ],
            options={
                'db_table': 'cart_table',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('house_name', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user')),
            ],
            options={
                'db_table': 'user_address_table',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=100)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.useraddress')),
            ],
            options={
                'db_table': 'order_table',
            },
        ),
    ]

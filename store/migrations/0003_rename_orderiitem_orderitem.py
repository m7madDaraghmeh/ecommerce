# Generated by Django 4.2.7 on 2024-02-13 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderIitem',
            new_name='OrderItem',
        ),
    ]
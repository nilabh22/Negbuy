# Generated by Django 3.1.4 on 2022-04-14 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0058_auto_20220414_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='main_image',
        ),
    ]

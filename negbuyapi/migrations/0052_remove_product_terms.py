# Generated by Django 3.1.4 on 2022-04-07 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0051_auto_20220407_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='terms',
        ),
    ]

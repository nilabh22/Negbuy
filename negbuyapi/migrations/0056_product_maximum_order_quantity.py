# Generated by Django 3.1.4 on 2022-04-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0055_remove_product_maximum_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='maximum_order_quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

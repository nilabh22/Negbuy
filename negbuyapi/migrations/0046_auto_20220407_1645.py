# Generated by Django 3.1.4 on 2022-04-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0045_auto_20220407_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=4, default='Add Price', max_digits=12, null=True),
        ),
    ]

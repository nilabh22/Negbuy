# Generated by Django 4.0.1 on 2022-02-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0035_alter_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('verified', 'verified'), ('under verification', 'under verification')], default='under verification', max_length=100),
        ),
    ]
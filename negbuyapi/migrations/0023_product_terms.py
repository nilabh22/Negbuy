# Generated by Django 4.0.1 on 2022-01-27 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0022_paymenttermfields_product_color_product_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='terms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.paymenttermfields'),
        ),
    ]

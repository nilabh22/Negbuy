# Generated by Django 4.0.1 on 2022-02-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0033_port_alter_paymenttermfields_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinventory',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

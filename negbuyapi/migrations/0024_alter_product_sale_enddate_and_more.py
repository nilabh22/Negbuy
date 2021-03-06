# Generated by Django 4.0.1 on 2022-01-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0023_product_terms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_enddate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_startdate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='Medium', max_length=100),
        ),
    ]

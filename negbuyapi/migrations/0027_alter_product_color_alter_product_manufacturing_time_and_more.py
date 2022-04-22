# Generated by Django 4.0.1 on 2022-01-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0026_remove_product_image_productimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, default='Black, Blue', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturing_time',
            field=models.CharField(blank=True, default='1 week', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='maximum_order_quantity',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='packing_address',
            field=models.CharField(blank=True, default='XYZ, India', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='packing_details',
            field=models.CharField(blank=True, default='ABC, India', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_enddate',
            field=models.CharField(blank=True, default='10 November 2022', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_startdate',
            field=models.CharField(blank=True, default='1 November 2022', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='transportation_port',
            field=models.CharField(blank=True, default='Mumbai Port', max_length=100, null=True),
        ),
    ]

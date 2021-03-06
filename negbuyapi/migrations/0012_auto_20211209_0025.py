# Generated by Django 3.2.6 on 2021-12-08 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0011_auto_20211208_2251'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product_category',
            new_name='productCategory',
        ),
        migrations.RenameModel(
            old_name='product_inventory',
            new_name='productInventory',
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.product')),
            ],
            options={
                'verbose_name_plural': 'Cart',
            },
        ),
    ]

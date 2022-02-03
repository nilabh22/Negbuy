# Generated by Django 4.0.1 on 2022-01-31 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0025_alter_product_category_id_alter_product_inventory_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.CreateModel(
            name='productImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to='Product_images')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.product')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
    ]
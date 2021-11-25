# Generated by Django 3.2.9 on 2021-11-25 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=4, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'product',
            },
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='product_inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'product_inventory',
            },
        ),
        migrations.CreateModel(
            name='userdb',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.TextField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('Merchant', 'Merchant'), ('Buyer', 'Buyer')], default='Buyer', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'userdb',
            },
        ),
        migrations.RemoveField(
            model_name='product_db',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='User_db',
        ),
        migrations.DeleteModel(
            name='Merchant_db',
        ),
        migrations.DeleteModel(
            name='Product_db',
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.product_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='inventory_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.product_inventory'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.userdb'),
        ),
    ]

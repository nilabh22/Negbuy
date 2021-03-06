# Generated by Django 4.0.1 on 2022-02-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0032_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Port',
            },
        ),
        migrations.AlterModelOptions(
            name='paymenttermfields',
            options={'verbose_name_plural': 'Payment Term Field'},
        ),
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name_plural': 'Product Image'},
        ),
    ]

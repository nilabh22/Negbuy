# Generated by Django 3.1.4 on 2022-04-17 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0068_primary_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primary_category',
            options={'verbose_name_plural': 'Primary Category'},
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='order_satus',
            new_name='order_status',
        ),
    ]
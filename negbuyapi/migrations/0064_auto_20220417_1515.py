# Generated by Django 3.1.4 on 2022-04-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0063_auto_20220417_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_satus',
            field=models.CharField(blank=True, choices=[('Running', 'Running'), ('Completed', 'Completed')], max_length=1000, null=True),
        ),
    ]
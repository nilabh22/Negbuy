# Generated by Django 3.1.4 on 2022-04-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0066_auto_20220417_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='feedback',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

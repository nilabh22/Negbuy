# Generated by Django 3.2.9 on 2021-11-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0002_auto_20211125_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

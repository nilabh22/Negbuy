# Generated by Django 3.1.4 on 2022-04-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0076_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
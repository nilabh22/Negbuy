# Generated by Django 3.2.6 on 2021-12-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0008_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 3.1.4 on 2022-04-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0069_auto_20220417_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact_data',
            options={'verbose_name_plural': 'Contact Data'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='feedback',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]

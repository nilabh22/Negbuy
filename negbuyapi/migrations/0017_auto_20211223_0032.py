# Generated by Django 3.2.6 on 2021-12-22 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0016_auto_20211223_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdb',
            name='address_line1',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='telephone',
        ),
    ]
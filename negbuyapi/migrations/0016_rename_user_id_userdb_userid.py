# Generated by Django 3.2.6 on 2021-12-16 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0015_auto_20211216_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdb',
            old_name='user_id',
            new_name='userid',
        ),
    ]
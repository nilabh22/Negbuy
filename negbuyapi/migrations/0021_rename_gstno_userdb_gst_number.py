# Generated by Django 3.2.6 on 2021-12-31 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0020_userdb_gstno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdb',
            old_name='gstNo',
            new_name='gst_number',
        ),
    ]

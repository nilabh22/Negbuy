# Generated by Django 3.2.6 on 2021-12-01 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procureapp', '0002_generated_rfq_rfq_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='procurement_user',
            old_name='address_line1',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='procurement_user',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='procurement_user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='procurement_user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='procurement_user',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='procurement_user',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='procurement_user',
            name='username',
        ),
    ]

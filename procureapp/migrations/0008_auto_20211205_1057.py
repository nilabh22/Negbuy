# Generated by Django 3.2.6 on 2021-12-05 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procureapp', '0007_auto_20211205_1047'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Generated_RFQ',
            new_name='generatedRFQ',
        ),
        migrations.RenameModel(
            old_name='Procurement_User',
            new_name='procurementUser',
        ),
    ]

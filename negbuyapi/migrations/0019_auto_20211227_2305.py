# Generated by Django 3.2.6 on 2021-12-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0018_auto_20211223_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdb',
            name='aadhaar',
        ),
        migrations.RemoveField(
            model_name='userdb',
            name='pan',
        ),
        migrations.AddField(
            model_name='userdb',
            name='document_verification',
            field=models.ImageField(blank=True, null=True, upload_to='Documents_images'),
        ),
        migrations.AddField(
            model_name='userdb',
            name='seller_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
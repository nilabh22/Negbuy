# Generated by Django 3.2.6 on 2021-12-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procureapp', '0005_procurement_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='generated_rfq',
            name='datetime',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
# Generated by Django 3.1.2 on 2022-05-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0072_auto_20220511_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer_questions',
            name='feedback',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
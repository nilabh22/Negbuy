# Generated by Django 3.2.6 on 2021-11-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procureapp', '0011_auto_20211128_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procure_userdb',
            name='id',
        ),
        migrations.AlterField(
            model_name='procure_userdb',
            name='user_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]

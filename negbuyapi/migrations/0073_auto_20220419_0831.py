# Generated by Django 3.1.4 on 2022-04-19 08:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0072_auto_20220419_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='id',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

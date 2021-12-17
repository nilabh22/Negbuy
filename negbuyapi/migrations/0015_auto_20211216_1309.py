# Generated by Django 3.2.6 on 2021-12-16 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('negbuyapi', '0014_rename_user_cart_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='negbuyapi.userdb'),
            preserve_default=False,
        ),
    ]
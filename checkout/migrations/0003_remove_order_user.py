# Generated by Django 4.1.3 on 2022-11-15 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]

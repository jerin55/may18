# Generated by Django 4.1.3 on 2023-04-19 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0035_alter_order_zip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='quanty',
        ),
    ]
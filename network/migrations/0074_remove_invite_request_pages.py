# Generated by Django 4.1.3 on 2023-05-18 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0073_remove_post_tages_n'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite_request',
            name='pages',
        ),
    ]

# Generated by Django 4.1.3 on 2023-04-21 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0043_post_viewers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='viewers',
        ),
    ]

# Generated by Django 4.1.3 on 2023-04-17 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0028_reviewreply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewreply',
            old_name='review',
            new_name='reviews',
        ),
    ]

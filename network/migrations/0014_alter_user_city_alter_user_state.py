# Generated by Django 4.1.3 on 2023-03-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_user_city_user_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

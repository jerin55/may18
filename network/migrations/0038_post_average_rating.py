# Generated by Django 4.1.3 on 2023-04-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0037_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True),
        ),
    ]

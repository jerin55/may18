# Generated by Django 4.1.3 on 2023-04-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0024_rename_offer_price_post_offer_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite_request',
            name='stat',
        ),
        migrations.AddField(
            model_name='invite_request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Joined', 'Joined'), ('Rejected', 'Rejected')], default='Pending', max_length=150),
        ),
    ]

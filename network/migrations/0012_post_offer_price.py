# Generated by Django 4.1.3 on 2023-03-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_remove_post_offer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='offer_price',
            field=models.IntegerField(blank=True, default=True, null=True),
        ),
    ]
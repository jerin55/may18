# Generated by Django 4.1.3 on 2023-03-31 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0020_page_city_page_facebook_link_page_linkedin_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='level2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrest_name', models.CharField(blank=True, max_length=255)),
                ('parent_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.intrest')),
            ],
        ),
        migrations.CreateModel(
            name='level3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrest_name', models.CharField(blank=True, max_length=255)),
                ('parent_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.intrest')),
                ('parent_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.level2')),
            ],
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-26 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_alter_post_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomid', models.CharField(blank=True, max_length=20)),
                ('datetime', models.DateTimeField(default=datetime.datetime)),
                ('user_s', models.CharField(blank=True, max_length=20)),
                ('user_r', models.CharField(blank=True, max_length=20)),
                ('value_s', models.CharField(max_length=1000)),
                ('value_r', models.CharField(max_length=1000)),
            ],
        ),
    ]

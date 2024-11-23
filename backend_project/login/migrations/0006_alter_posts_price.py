# Generated by Django 5.1.2 on 2024-10-23 12:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_rename_date_posts_datetime_rename_title_posts_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='price',
            field=models.IntegerField(default=False, validators=[django.core.validators.MaxValueValidator(6)]),
        ),
    ]
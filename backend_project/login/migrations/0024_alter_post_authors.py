# Generated by Django 5.1.2 on 2024-10-26 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_remove_post_authors_post_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='authors',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='login.author'),
        ),
    ]
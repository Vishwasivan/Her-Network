# Generated by Django 5.1.2 on 2024-10-23 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='title',
            new_name='titles',
        ),
    ]
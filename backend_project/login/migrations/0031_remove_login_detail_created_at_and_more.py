# Generated by Django 5.1.3 on 2024-11-23 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0030_login_detail_is_verified_login_detail_retry_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_detail',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='login_detail',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='login_detail',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='login_detail',
            name='retry_count',
        ),
    ]
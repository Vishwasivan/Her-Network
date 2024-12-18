# Generated by Django 5.1.3 on 2024-11-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0029_login_detail_created_at_login_detail_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_detail',
            name='is_verified',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='login_detail',
            name='retry_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

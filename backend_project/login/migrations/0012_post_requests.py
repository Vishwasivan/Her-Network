# Generated by Django 5.1.2 on 2024-10-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_alter_post_datetime_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='requests',
            field=models.CharField(blank=True, default='post', max_length=50, null=True),
        ),
    ]
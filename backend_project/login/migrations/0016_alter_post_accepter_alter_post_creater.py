# Generated by Django 5.1.2 on 2024-10-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_alter_post_accepter_alter_post_creater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='accepter',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='creater',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]

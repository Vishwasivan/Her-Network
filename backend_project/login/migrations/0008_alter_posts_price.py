# Generated by Django 5.1.2 on 2024-10-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_posts_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]

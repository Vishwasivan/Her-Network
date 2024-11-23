# Generated by Django 5.1.2 on 2024-10-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(),
        ),
    ]

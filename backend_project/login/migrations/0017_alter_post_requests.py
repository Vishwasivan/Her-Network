# Generated by Django 5.1.2 on 2024-10-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_alter_post_accepter_alter_post_creater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='requests',
            field=models.CharField(blank=True, default=list, max_length=50, null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='translators',
            name='user_name',
            field=models.CharField(default='Karen', max_length=20),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_translators_user_name_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translators',
            name='user_name',
            field=models.CharField(default='Karen', max_length=20),
        ),
    ]

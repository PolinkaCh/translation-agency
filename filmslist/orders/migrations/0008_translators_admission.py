# Generated by Django 4.1.3 on 2022-11-11 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='translators',
            name='admission',
            field=models.ForeignKey(blank=True, help_text='Enter your types of admission', null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.translationtypes'),
        ),
    ]

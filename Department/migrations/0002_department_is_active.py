# Generated by Django 3.1.5 on 2021-01-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]
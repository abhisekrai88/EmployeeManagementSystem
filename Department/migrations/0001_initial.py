# Generated by Django 3.1.5 on 2021-01-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_ID', models.AutoField(primary_key=True, serialize=False, verbose_name='Department ID')),
                ('department_name', models.CharField(max_length=30, verbose_name='Department Name')),
            ],
        ),
    ]
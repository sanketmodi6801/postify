# Generated by Django 3.2.6 on 2022-10-29 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clip', '0002_auto_20221029_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='category',
            name='img',
        ),
    ]

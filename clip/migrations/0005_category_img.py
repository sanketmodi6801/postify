# Generated by Django 3.2.6 on 2022-11-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clip', '0004_category_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
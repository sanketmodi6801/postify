# Generated by Django 3.2.6 on 2022-10-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default='', upload_to='static/insta'),
        ),
    ]

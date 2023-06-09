# Generated by Django 3.2.6 on 2022-10-19 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default=' ', max_length=10000)),
                ('name', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clip.category')),
            ],
        ),
    ]

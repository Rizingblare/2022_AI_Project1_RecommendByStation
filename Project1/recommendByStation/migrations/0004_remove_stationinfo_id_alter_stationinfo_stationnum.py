# Generated by Django 4.0.5 on 2022-06-15 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendByStation', '0003_stationinfo_stationbikestorage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='stationinfo',
            name='stationNum',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]

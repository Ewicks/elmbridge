# Generated by Django 3.2 on 2022-10-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_auto_20221004_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='age',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.CharField(default=True, max_length=200),
        ),
    ]

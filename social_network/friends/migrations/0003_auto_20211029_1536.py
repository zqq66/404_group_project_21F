# Generated by Django 3.1.6 on 2021-10-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20211029_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='respond_status',
            field=models.BooleanField(default=True),
        ),
    ]

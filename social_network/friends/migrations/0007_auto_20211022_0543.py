# Generated by Django 3.1.6 on 2021-10-22 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0006_auto_20211022_0539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='request_id',
            new_name='requestid',
        ),
    ]

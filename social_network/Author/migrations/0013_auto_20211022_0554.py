# Generated by Django 3.1.6 on 2021-10-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0012_auto_20211022_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'PUBLIC'), (3, 'PRIVATE'), (2, 'FRIEND ONLY'), (4, 'UNLISTED')], default=1),
        ),
    ]

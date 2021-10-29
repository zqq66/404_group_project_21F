# Generated by Django 3.2.8 on 2021-10-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0011_alter_post_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_image'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]

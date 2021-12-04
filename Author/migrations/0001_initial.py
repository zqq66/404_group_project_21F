# Generated by Django 3.2.8 on 2021-12-04 13:12

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('host', models.URLField(default='', primary_key=True, serialize=False, unique=True)),
                ('allow_connection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_registration', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('profile_image', models.TextField()),
                ('email', models.CharField(max_length=20, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('u_phone', models.CharField(blank=True, default='', max_length=20, verbose_name='phone_number')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('github', models.CharField(blank=True, max_length=100)),
                ('url', models.URLField(editable=False)),
                ('host', models.URLField(editable=False)),
                ('api_url', models.URLField(editable=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
                'db_table': 'sys_user_info',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('url', models.URLField(editable=False)),
                ('api_url', models.URLField(editable=False)),
                ('source', models.URLField(blank=True)),
                ('origin', models.URLField(blank=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('contentType', models.TextField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], default='text/plain')),
                ('content', models.TextField(blank=True)),
                ('categories', models.CharField(blank=True, max_length=500)),
                ('count', models.IntegerField(default=0)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('visibility', models.SmallIntegerField(choices=[(1, 'PUBLIC'), (2, 'FRIEND ONLY'), (3, 'PRIVATE'), (4, 'UNLISTED')], default=1)),
                ('unlisted', models.BooleanField(default=False)),
                ('select_user', models.CharField(blank=True, max_length=20)),
                ('image', models.TextField()),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'posts',
                'ordering': ('published',),
            },
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.JSONField(default=list, max_length=10000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inbox', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

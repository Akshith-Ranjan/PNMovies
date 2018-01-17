# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-17 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('username', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('mid', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('cast', models.TextField(blank=True, null=True)),
                ('crew', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'credits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('budget', models.TextField(blank=True, null=True)),
                ('genres', models.TextField(blank=True, null=True)),
                ('homepage', models.TextField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('original_language', models.TextField(blank=True, null=True)),
                ('original_title', models.TextField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('popularity', models.TextField(blank=True, null=True)),
                ('production_companies', models.TextField(blank=True, null=True)),
                ('production_countries', models.TextField(blank=True, null=True)),
                ('release_date', models.TextField(blank=True, null=True)),
                ('revenue', models.TextField(blank=True, null=True)),
                ('runtime', models.TextField(blank=True, null=True)),
                ('spoken_languages', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('tagline', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('vote_average', models.TextField(blank=True, null=True)),
                ('vote_count', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
    ]

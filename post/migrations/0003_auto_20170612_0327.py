# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 03:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20170612_0311'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'post_post_like_users',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', through='post.PostLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AddField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

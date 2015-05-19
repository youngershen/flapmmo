# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WechatUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('username', models.CharField(unique=True, max_length=255, verbose_name='username', db_index=True)),
                ('status', models.IntegerField(default=0, verbose_name='status status', choices=[(b'FOLLOWED', 0), (b'UNFOLLOWED', 1)])),
                ('score', models.IntegerField(default=0, verbose_name='score')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'wechat user',
                'verbose_name_plural': 'wechat users',
            },
        ),
    ]

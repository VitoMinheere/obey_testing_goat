# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-17 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='email',
            field=models.EmailField(default='a@b.com', max_length=254),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homevideo',
            name='file',
            field=models.FileField(default=False, upload_to='uploads/videos'),
            preserve_default=False,
        ),
    ]
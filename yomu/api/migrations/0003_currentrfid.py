# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_album_rfid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentRfid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
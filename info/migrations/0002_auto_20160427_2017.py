# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-27 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Faq',
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]

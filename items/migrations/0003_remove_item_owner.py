# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-11-02 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='owner',
        ),
    ]

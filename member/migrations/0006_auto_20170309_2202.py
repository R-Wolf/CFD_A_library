# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 16:32


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20170306_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='Dues',
        ),
        migrations.RemoveField(
            model_name='member',
            name='Status',
        ),
    ]

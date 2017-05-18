# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 17:10


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20170306_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Fine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='Status',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='books',
            field=models.ManyToManyField(null=True, to='catalogue.Post'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 12:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_post_member_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='member_Name',
            field=models.CharField(default=b'Nill', max_length=140, null=True),
        ),
    ]

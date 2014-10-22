# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micro_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clients',
            name='blood_group',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='mobile',
            field=models.CharField(default=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'/users/'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='pincode',
            field=models.CharField(default=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='signature',
            field=models.ImageField(null=True, upload_to=b'/signature/'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micro_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=b'2000-06-04', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=b'', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(default=b'0', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.BigIntegerField(default=b'0', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('opening_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('phone_number', models.BigIntegerField()),
                ('pincode', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('created_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=255, unique=True, null=True)),
                ('account_type', models.CharField(max_length=20, choices=[(b'SavingsAccount', b'SavingsAccount'), (b'LoanAccount', b'LoanAccount')])),
                ('account_number', models.CharField(unique=True, max_length=50)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('clent_role', models.CharField(max_length=20, choices=[(b'FirstLeader', b'FirstLeader'), (b'SecondLeader', b'SecondLeader'), (b'GroupMember', b'GroupMember')])),
                ('occupation', models.CharField(max_length=200)),
                ('annual_income', models.BigIntegerField()),
                ('joined_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('mobile', models.BigIntegerField()),
                ('pincode', models.BigIntegerField()),
                ('photo', models.ImageField(upload_to=b'/home/swetha/microfinance/microfinance/images/users')),
                ('signature', models.ImageField(upload_to=b'/home/swetha/microfinance/microfinance/images/signature')),
                ('is_active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('account_type', models.CharField(max_length=20, choices=[(b'SavingsAccount', b'SavingsAccount'), (b'LoanAccount', b'LoanAccount')])),
                ('account_number', models.CharField(unique=True, max_length=50)),
                ('activation_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
                ('clients', models.ManyToManyField(to='micro_admin.Clients')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('first_name', models.CharField(default=b'', max_length=100)),
                ('last_name', models.CharField(default=b'', max_length=100)),
                ('gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('user_roles', models.CharField(max_length=20, choices=[(b'BranchManager', b'BranchManager'), (b'LoanOfficer', b'LoanOfficer'), (b'Cashier', b'Cashier')])),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('mobile', models.BigIntegerField()),
                ('pincode', models.BigIntegerField()),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='centers',
            name='groups',
            field=models.ManyToManyField(to='micro_admin.Groups'),
            preserve_default=True,
        ),
    ]

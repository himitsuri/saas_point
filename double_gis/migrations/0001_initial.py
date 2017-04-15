# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('social', models.CharField(blank=True, max_length=100, null=True)),
                ('main_category', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
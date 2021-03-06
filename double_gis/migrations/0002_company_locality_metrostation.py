# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('double_gis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('name_synonyms', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('main_category', models.TextField(blank=True, null=True)),
                ('sub_category', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('time_points_json', models.TextField(blank=True, null=True)),
                ('coordinates_json', models.TextField(blank=True, null=True)),
                ('metro_distances_json', models.TextField(blank=True, null=True)),
                ('contracts_json', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetroStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('coordinates_json', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

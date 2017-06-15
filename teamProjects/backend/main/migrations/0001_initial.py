# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoiveTimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_loc', models.CharField(max_length=50)),
                ('movie_date', models.CharField(blank=True, max_length=50)),
                ('movie_time', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_n', models.CharField(blank=True, max_length=300)),
                ('movie_actor', models.CharField(blank=True, max_length=50)),
                ('movie_director', models.CharField(blank=True, max_length=30)),
                ('movie_pic_loc', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_name', models.CharField(max_length=30)),
                ('theater_phone', models.CharField(blank=True, max_length=15)),
                ('theater_loc', models.CharField(blank=True, max_length=100)),
                ('theater_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Theater'),
        ),
        migrations.AddField(
            model_name='moivetimetable',
            name='movie_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie'),
        ),
    ]

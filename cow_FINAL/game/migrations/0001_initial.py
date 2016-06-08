# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hp', models.IntegerField(default=100)),
                ('Mp', models.IntegerField(default=100)),
                ('Charactercard', models.IntegerField(default=0)),
                ('Activecard1', models.IntegerField(default=0)),
                ('Activecard2', models.IntegerField(default=0)),
                ('Activecard3', models.IntegerField(default=0)),
                ('position_x', models.IntegerField(default=0)),
                ('position_y', models.IntegerField(default=2)),
                ('win', models.IntegerField(default=0)),
                ('draw', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
                ('mynum', models.CharField(max_length=10)),
                ('enemy', models.CharField(max_length=10)),
                ('field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='startplayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.IntegerField(default=0)),
                ('winer', models.CharField(max_length=10)),
                ('player1', models.CharField(max_length=10)),
                ('player2', models.CharField(max_length=10)),
            ],
        ),
    ]

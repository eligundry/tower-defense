# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_tile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameTile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game', models.ForeignKey(to='game.Game')),
                ('tile', models.ForeignKey(to='game.Tile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='tiles',
            field=models.ManyToManyField(to='game.Tile', through='game.GameTile'),
            preserve_default=True,
        ),
    ]

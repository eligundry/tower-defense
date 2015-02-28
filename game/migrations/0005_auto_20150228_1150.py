# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_tower'),
    ]

    operations = [
        migrations.CreateModel(
            name='TileTower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tile', models.ForeignKey(to='game.GameTile')),
                ('tower', models.ForeignKey(to='game.Tower')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gametile',
            name='tower',
            field=models.ManyToManyField(to='game.Tower', through='game.TileTower'),
            preserve_default=True,
        ),
    ]

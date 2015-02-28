# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20150228_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='TileMonster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hp', models.IntegerField()),
                ('monster', models.ForeignKey(to='game.Monster')),
                ('tile', models.ForeignKey(to='game.GameTile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gametile',
            name='monster',
            field=models.ManyToManyField(to='game.Monster', null=True, through='game.TileMonster'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20150228_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=50)),
                ('max_hp', models.IntegerField()),
                ('attack_range', models.IntegerField(null=True)),
                ('movement_range', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='tower',
            old_name='hp',
            new_name='max_hp',
        ),
        migrations.AddField(
            model_name='tiletower',
            name='hp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gametile',
            name='tower',
            field=models.ManyToManyField(to='game.Tower', null=True, through='game.TileTower'),
            preserve_default=True,
        ),
    ]

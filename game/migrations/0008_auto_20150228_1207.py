# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20150228_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='height',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='width',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tower',
            name='attack_range',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]

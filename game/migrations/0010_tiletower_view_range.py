# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20150228_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiletower',
            name='view_range',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

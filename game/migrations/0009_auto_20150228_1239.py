# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20150228_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tower',
            old_name='attack_range',
            new_name='view_range',
        ),
        migrations.AddField(
            model_name='monster',
            name='damage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tower',
            name='class_name',
            field=models.CharField(default='blah', max_length=50),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_tiletower_view_range'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tile',
            options={'ordering': ['y_coordinate', 'x_coordinate']},
        ),
    ]

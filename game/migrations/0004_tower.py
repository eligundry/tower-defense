# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20150228_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('hp', models.IntegerField()),
                ('attack_range', models.IntegerField()),
                ('damage', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

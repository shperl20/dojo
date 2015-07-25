# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0009_auto_20150614_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimadvisor',
            name='current_flag',
            field=models.CharField(default='N', max_length=1),
            preserve_default=False,
        ),
    ]

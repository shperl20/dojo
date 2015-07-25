# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0005_remove_advisor_dly_advisor_dashboard_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='dly_advisor_dashboard_key',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]

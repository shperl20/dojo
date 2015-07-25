# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0004_auto_20150608_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='dly_advisor_dashboard_key',
        ),
    ]

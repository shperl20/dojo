# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0007_auto_20150608_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisors',
            name='no_of_positive_surveys',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

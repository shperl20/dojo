# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyadvisor',
            name='advisor_email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyadvisor',
            name='advisor_first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyadvisor',
            name='advisor_last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]

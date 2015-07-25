# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0003_auto_20150607_0347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contactData',
        ),
        migrations.AddField(
            model_name='advisor',
            name='acw',
            field=models.DecimalField(default='', max_digits=20, decimal_places=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='channel_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='contact_cbr',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='contact_language',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='ctgry_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='dly_advisor_dashboard_key',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='event_date',
            field=models.DateField(default='1900-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='fscl_month_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='fscl_year_nbr',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='handle_time',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='no_of_resolutions_surveys',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='no_survey_response_received',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='platform_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='product_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='total_no_of_handled',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advisor',
            name='week_of',
            field=models.DateField(default='1900-01-01'),
            preserve_default=False,
        ),
    ]

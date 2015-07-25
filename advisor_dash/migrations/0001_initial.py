# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dailyAdvisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dly_advisor_dashboard_key', models.IntegerField()),
                ('event_date', models.DateField()),
                ('week_of', models.DateField()),
                ('fscl_year', models.IntegerField()),
                ('fscl_month', models.CharField(max_length=20)),
                ('channel_name', models.CharField(max_length=100)),
                ('contact_language', models.CharField(max_length=100)),
                ('ctgry_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('platform_name', models.CharField(max_length=100)),
                ('advisor_key', models.IntegerField()),
                ('staff_grp', models.CharField(max_length=255)),
                ('manager_first_name', models.CharField(max_length=100)),
                ('manager_last_name', models.CharField(max_length=100)),
                ('advisor_language', models.CharField(max_length=100)),
                ('advisor_tier', models.CharField(max_length=100)),
                ('contact_cbr', models.CharField(max_length=255)),
                ('vendor_name', models.CharField(max_length=255)),
                ('region_name', models.CharField(max_length=100)),
                ('acw', models.DecimalField(max_digits=20, decimal_places=7)),
                ('handle_time', models.DecimalField(max_digits=20, decimal_places=7)),
                ('total_no_of_handled', models.IntegerField()),
                ('no_survey_response_received', models.IntegerField()),
                ('no_of_resolutions_surveys', models.IntegerField()),
            ],
        ),
    ]

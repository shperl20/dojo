# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0002_auto_20150607_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advisor_key', models.IntegerField()),
                ('advisor_email', models.CharField(max_length=255)),
                ('advisor_first_name', models.CharField(max_length=255)),
                ('advisor_last_name', models.CharField(max_length=255)),
                ('staff_grp', models.CharField(max_length=255)),
                ('manager_first_name', models.CharField(max_length=100)),
                ('manager_last_name', models.CharField(max_length=100)),
                ('advisor_language', models.CharField(max_length=100)),
                ('advisor_tier', models.CharField(max_length=100)),
                ('vendor_name', models.CharField(max_length=255)),
                ('region_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='contactData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dly_advisor_dashboard_key', models.IntegerField()),
                ('advisor_key', models.IntegerField()),
                ('no_survey_response_received', models.IntegerField()),
                ('total_no_of_handled', models.IntegerField()),
                ('handle_time', models.DecimalField(max_digits=20, decimal_places=7)),
                ('no_of_resolutions_surveys', models.IntegerField()),
                ('acw', models.DecimalField(max_digits=20, decimal_places=7)),
                ('contact_cbr', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=100)),
                ('platform_name', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('week_of', models.DateField()),
                ('fscl_year', models.IntegerField()),
                ('fscl_month', models.CharField(max_length=20)),
                ('channel_name', models.CharField(max_length=100)),
                ('ctgry_name', models.CharField(max_length=100)),
                ('contact_language', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='dailyAdvisor',
        ),
    ]

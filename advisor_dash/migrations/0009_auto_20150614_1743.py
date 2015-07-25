# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor_dash', '0008_advisors_no_of_positive_surveys'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimAdvisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advisor_key', models.IntegerField()),
                ('advisor_email', models.CharField(max_length=255)),
                ('advisor_first_name', models.CharField(max_length=255)),
                ('advisor_last_name', models.CharField(max_length=255)),
                ('staff_grp', models.CharField(max_length=255)),
                ('manager_first_name', models.CharField(max_length=255)),
                ('manager_last_name', models.CharField(max_length=255)),
                ('advisor_language', models.CharField(max_length=100)),
                ('advisor_tier', models.CharField(max_length=100)),
                ('vendor_name', models.CharField(max_length=255)),
                ('region_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='advisors',
            name='advisor_key',
            field=models.ForeignKey(to='advisor_dash.DimAdvisor'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-12-16 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0024_vehiclecategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('POA', 'Pay on arrival'), ('ONL', 'Online')], default='POA', max_length=3, null=True),
        ),
    ]

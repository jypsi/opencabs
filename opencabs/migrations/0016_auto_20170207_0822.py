# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0015_auto_20170206_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_mobile',
            field=models.CharField(db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pnr',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='mobile',
            field=models.CharField(db_index=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='code',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='number',
            field=models.CharField(db_index=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicleratecategory',
            name='name',
            field=models.CharField(db_index=True, max_length=30, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('code', 'vehicle_category')]),
        ),
        migrations.AlterUniqueTogether(
            name='vehicleratecategory',
            unique_together=set([('name', 'category')]),
        ),
    ]

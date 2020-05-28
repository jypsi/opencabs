# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-03-08 10:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0010_auto_20190901_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='accounts_last_updated',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='accounts_last_updated_by',
            field=models.ForeignKey(blank=True, help_text='Accountant who last updated this entry', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-17 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0063_add_slack_webhook_url_field_in_challenge_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengephase',
            name='is_restricted_to_select_one_submission',
            field=models.BooleanField(default=False),
        ),
    ]

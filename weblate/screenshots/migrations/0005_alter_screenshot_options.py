# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.2 on 2021-05-12 19:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("screenshots", "0004_auto_20201002_1423"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="screenshot",
            options={
                "verbose_name": "Screenshot",
                "verbose_name_plural": "Screenshots",
            },
        ),
    ]

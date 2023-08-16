# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.3 on 2023-08-04 11:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0029_jsonfield"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auditlog",
            name="params",
        ),
    ]

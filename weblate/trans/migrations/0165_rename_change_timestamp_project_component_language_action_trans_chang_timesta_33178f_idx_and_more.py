# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.3 on 2023-01-19 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0164_alter_component_push_alter_component_repo"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="change",
            new_name="trans_chang_timesta_33178f_idx",
            old_fields=("timestamp", "project", "component", "language", "action"),
        ),
        migrations.RenameIndex(
            model_name="change",
            new_name="trans_chang_action_27fd77_idx",
            old_fields=("action", "translation", "timestamp"),
        ),
    ]

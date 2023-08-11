# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.7 on 2023-05-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "trans",
            "0165_rename_change_timestamp_project_component_language_action_trans_chang_timesta_33178f_idx_and_more",
        ),
        ("weblate_auth", "0026_remove_selection_lists"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="components",
            field=models.ManyToManyField(
                blank=True,
                help_text="Empty selection grants access to all components in project scope.",
                to="trans.component",
                verbose_name="Components",
            ),
        ),
    ]

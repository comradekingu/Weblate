# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.7 on 2020-09-07 11:39

import django.db.models.deletion
from django.db import migrations, models

import weblate.lang.models


class Migration(migrations.Migration):
    dependencies = [
        ("lang", "0010_auto_20200627_0508"),
        ("trans", "0096_fix_enforced_checks"),
        ("glossary", "0005_set_source_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="component",
            name="source_language",
            field=models.ForeignKey(
                default=weblate.lang.models.get_default_lang,
                help_text="Language used for source strings in all components",
                on_delete=django.db.models.deletion.CASCADE,
                to="lang.Language",
                verbose_name="Source language",
            ),
        ),
    ]

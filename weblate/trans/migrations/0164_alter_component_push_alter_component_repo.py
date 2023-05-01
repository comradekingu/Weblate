# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1.7 on 2023-03-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0163_update_indexes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="push",
            field=models.CharField(
                blank=True,
                help_text="The URL of a repository to push to. (Pushing is turned off if left empty.)",
                max_length=300,
                verbose_name="Repository push URL",
            ),
        ),
        migrations.AlterField(
            model_name="component",
            name="repo",
            field=models.CharField(
                help_text="The URL of a repository. Use weblate://project/component to use the settings of an existing Weblate component.",
                max_length=300,
                verbose_name="Source-code repository",
            ),
        ),
    ]

# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.5 on 2020-06-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lang", "0009_auto_20200521_0753"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plural",
            name="type",
            field=models.IntegerField(
                choices=[
                    (0, "None"),
                    (1, "One/other (classic plural)"),
                    (2, "One/few/other (Slavic languages)"),
                    (3, "Arabic languages"),
                    (11, "Zero/one/other"),
                    (4, "One/two/other"),
                    (14, "One/other/two"),
                    (6, "One/two/few/other"),
                    (13, "Other/one/two/few"),
                    (5, "One/two/three/other"),
                    (7, "One/other/zero"),
                    (8, "One/few/many/other"),
                    (9, "Two/other"),
                    (10, "One/two/few/many/other"),
                    (12, "Zero/one/two/few/many/other"),
                    (666, "Unknown"),
                ],
                default=666,
                editable=False,
                verbose_name="Plural type",
            ),
        ),
    ]

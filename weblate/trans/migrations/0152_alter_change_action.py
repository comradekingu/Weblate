# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.1a1 on 2022-07-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0151_project_machinery_settings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="change",
            name="action",
            field=models.IntegerField(
                choices=[
                    (0, "Resource update"),
                    (1, "Translation completed"),
                    (2, "Translation changed"),
                    (5, "New translation"),
                    (3, "Comment added"),
                    (4, "Suggestion added"),
                    (6, "Automatic translation"),
                    (7, "Suggestion accepted"),
                    (8, "Translation reverted"),
                    (9, "Translation uploaded"),
                    (13, "New source string"),
                    (14, "Component locked"),
                    (15, "Component unlocked"),
                    (16, "Found duplicated string"),
                    (17, "Committed changes"),
                    (18, "Pushed changes"),
                    (19, "Reset repository"),
                    (20, "Merged repository"),
                    (21, "Rebased repository"),
                    (22, "Failed merge on repository"),
                    (23, "Failed rebase on repository"),
                    (28, "Failed push on repository"),
                    (24, "Parse error"),
                    (25, "Removed translation"),
                    (26, "Suggestion removed"),
                    (27, "Search and replace"),
                    (29, "Suggestion removed during cleanup"),
                    (30, "Source string changed"),
                    (31, "New string added"),
                    (32, "Bulk status change"),
                    (33, "Changed visibility"),
                    (34, "Added user"),
                    (35, "Removed user"),
                    (36, "Translation approved"),
                    (37, "Marked for edit"),
                    (38, "Removed component"),
                    (39, "Removed project"),
                    (40, "Found duplicated language"),
                    (41, "Renamed project"),
                    (42, "Renamed component"),
                    (43, "Moved component"),
                    (44, "New string to translate"),
                    (45, "New contributor"),
                    (46, "New announcement"),
                    (47, "New alert"),
                    (48, "Added new language"),
                    (49, "Requested new language"),
                    (50, "Created project"),
                    (51, "Created component"),
                    (52, "Invited user"),
                    (53, "Received repository notification"),
                    (54, "Replaced file by upload"),
                    (55, "License changed"),
                    (56, "Contributor agreement changed"),
                    (57, "Screnshot added"),
                    (58, "Screnshot uploaded"),
                    (59, "String updated in the repository"),
                    (60, "Add-on installed"),
                    (61, "Add-on configuration changed"),
                    (62, "Add-on uninstalled"),
                ],
                db_index=True,
                default=2,
            ),
        ),
    ]

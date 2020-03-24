# Generated by Django 1.11.17 on 2019-01-31 12:45

from django.db import migrations

from weblate.addons.events import EVENT_POST_COMMIT, EVENT_PRE_PUSH
from weblate.addons.utils import adjust_addon_events


def update_squash_addon(apps, schema_editor):
    """Update events setup for weblate.git.squash addon."""
    adjust_addon_events(
        apps,
        schema_editor,
        ["weblate.git.squash"],
        [EVENT_POST_COMMIT],
        [EVENT_PRE_PUSH],
    )


class Migration(migrations.Migration):

    dependencies = [("addons", "0010_auto_20181214_1232")]

    operations = [migrations.RunPython(update_squash_addon, elidable=True)]

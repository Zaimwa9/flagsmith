# Generated by Django 3.2.16 on 2022-12-08 11:02

from django.db import migrations

from organisations.permissions.permissions import MANAGE_USER_GROUPS
from permissions.models import ORGANISATION_PERMISSION_TYPE


def create_permissions(apps, schema_editor):  # type: ignore[no-untyped-def]
    permission_model_class = apps.get_model("permissions", "PermissionModel")

    permission_model_class.objects.get_or_create(
        key=MANAGE_USER_GROUPS,
        description="Allows the user to manage the groups in the organisation and their members.",
        type=ORGANISATION_PERMISSION_TYPE,
    )


def remove_permissions(apps, schema_editor):  # type: ignore[no-untyped-def]
    apps.get_model("permissions", "PermissionModel").objects.filter(
        key__in=[MANAGE_USER_GROUPS]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0006_add_manage_segments_permission"),
    ]

    operations = [
        migrations.RunPython(create_permissions, reverse_code=remove_permissions)
    ]

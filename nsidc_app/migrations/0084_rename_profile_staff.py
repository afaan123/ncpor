# Generated by Django 4.1 on 2022-09-06 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nsidc_app", "0083_delete_researchgrant"),
    ]

    operations = [
        migrations.RenameModel(old_name="profile", new_name="staff",),
    ]
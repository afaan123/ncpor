# Generated by Django 4.1 on 2022-09-06 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nsidc_app", "0075_delete_scientificpublication"),
    ]

    operations = [
        migrations.DeleteModel(name="scientificExpedition",),
    ]
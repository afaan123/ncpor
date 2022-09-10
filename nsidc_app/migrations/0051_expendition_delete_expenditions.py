# Generated by Django 4.1 on 2022-09-03 06:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nsidc_app", "0050_expenditions_information_services_management_support"),
    ]

    operations = [
        migrations.CreateModel(
            name="expendition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", ckeditor.fields.RichTextField()),
                ("slug", models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(name="expenditions",),
    ]
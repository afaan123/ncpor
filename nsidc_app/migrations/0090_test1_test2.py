# Generated by Django 4.1 on 2022-09-06 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nsidc_app", "0089_staff_content_staff_current_research_activities_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="test1",
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
                ("name", models.CharField(max_length=255)),
                ("designation", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="test2",
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
                ("name", models.CharField(max_length=255)),
                (
                    "test",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nsidc_app.test1",
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 4.1 on 2022-09-06 09:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nsidc_app", "0088_rename_news_new"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff",
            name="content",
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name="staff",
            name="current_research_activities",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="staff",
            name="field_of_specilization",
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nsidc_app", "0092_readmore"),
    ]

    operations = [
        migrations.AddField(
            model_name="readmore",
            name="title",
            field=models.CharField(max_length=200, null=True),
        ),
    ]

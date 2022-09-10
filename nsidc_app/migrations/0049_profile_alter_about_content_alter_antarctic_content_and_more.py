# Generated by Django 4.1 on 2022-09-02 14:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nsidc_app", "0048_remove_dataclass_content_dataclass_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="profile",
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
                ("email_id", models.CharField(max_length=255)),
                ("desk_no", models.CharField(max_length=255)),
                ("photo", models.ImageField(upload_to="photos/%Y/%m/%d/")),
            ],
        ),
        migrations.AlterField(
            model_name="about", name="content", field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="antarctic",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="arctic", name="content", field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="atmosphere",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="eventclass",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="geosciences",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="himalaya",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="informationresearch",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="mineralresources",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="newsclass",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="polarenvironments",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="polaroceans",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="polarscience",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="research",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="researchgrant",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="researchscientist",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="scientificexpedition",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="scientificpublication",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="southern_ocean",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
# Generated by Django 4.0.5 on 2022-08-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsidc_app', '0046_alter_about_id_alter_antarctic_id_alter_arctic_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='webmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('link', models.URLField(verbose_name='')),
            ],
        ),
    ]
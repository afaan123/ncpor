# Generated by Django 3.1.14 on 2022-07-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsidc_app', '0004_delete_society'),
    ]

    operations = [
        migrations.CreateModel(
            name='informationResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='researchGrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='researchScientist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='scientificExpedition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='scientificPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='research',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
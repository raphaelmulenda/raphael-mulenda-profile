# Generated by Django 3.2.7 on 2021-09-24 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20210923_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_level', models.CharField(max_length=50)),
                ('study_field', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('university_url', models.URLField(blank=True)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('work_position', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('job_description', models.TextField(validators=[django.core.validators.MinLengthValidator(20)])),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_area', models.CharField(max_length=50)),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.CharField(max_length=100)),
                ('project_url', models.URLField(blank=True)),
                ('project_image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_area', models.CharField(max_length=200)),
                ('service_url', models.CharField(max_length=50)),
                ('service_description', models.TextField(validators=[django.core.validators.MinLengthValidator(15)])),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='skill',
        ),
    ]

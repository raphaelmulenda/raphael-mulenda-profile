# Generated by Django 3.2.7 on 2021-09-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_portfolio_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
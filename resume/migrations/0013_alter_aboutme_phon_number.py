# Generated by Django 3.2.7 on 2021-09-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_alter_aboutme_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='phon_number',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_auto_20210924_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=120)),
                ('contact_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('contact_message', models.TextField()),
            ],
        ),
    ]
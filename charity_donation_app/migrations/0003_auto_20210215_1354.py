# Generated by Django 3.1.6 on 2021-02-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation_app', '0002_donation_is_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
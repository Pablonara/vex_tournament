# Generated by Django 5.0 on 2023-12-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament_site', '0002_alter_field_matches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='time',
            field=models.TimeField(),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-13 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aircraft',
            old_name='manufaturer',
            new_name='manufacturer',
        ),
    ]

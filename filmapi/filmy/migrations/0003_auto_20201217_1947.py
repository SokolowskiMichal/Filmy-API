# Generated by Django 3.1.3 on 2020-12-17 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0002_auto_20201217_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='data',
            new_name='data_premiery',
        ),
    ]
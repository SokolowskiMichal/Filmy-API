# Generated by Django 3.1.3 on 2020-12-17 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0004_auto_20201217_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='dataPremiery',
            new_name='rok',
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-05 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_auto_20210805_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='is_requird',
            new_name='is_required',
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-05 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='created_at',
            new_name='activity_at',
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-09 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200309_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='value',
            new_name='log_value',
        ),
    ]
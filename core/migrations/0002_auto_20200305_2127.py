# Generated by Django 3.0.4 on 2020-03-05 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='created_at',
        ),
        migrations.AddField(
            model_name='log',
            name='activity_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-31 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaraj_builder', '0012_auto_20190831_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='enquiry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 1, 1, 55, 13, 745067)),
        ),
        migrations.AlterField(
            model_name='record',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 1, 1, 55, 13, 746067)),
        ),
    ]

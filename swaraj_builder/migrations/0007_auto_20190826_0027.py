# Generated by Django 2.2.4 on 2019-08-25 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaraj_builder', '0006_auto_20190826_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='enquiry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 26, 0, 27, 43, 992806)),
        ),
        migrations.AlterField(
            model_name='record',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 26, 0, 27, 43, 993312)),
        ),
    ]
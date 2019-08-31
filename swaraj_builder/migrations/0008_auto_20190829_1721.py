# Generated by Django 2.2.4 on 2019-08-29 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaraj_builder', '0007_auto_20190826_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='enquiry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 29, 17, 21, 13, 433419)),
        ),
        migrations.AlterField(
            model_name='quest',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 29, 17, 21, 13, 434429)),
        ),
        migrations.AlterField(
            model_name='record',
            name='happy_clients',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='projects_completed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='total_tasks',
            field=models.IntegerField(),
        ),
    ]
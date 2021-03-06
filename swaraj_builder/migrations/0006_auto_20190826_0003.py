# Generated by Django 2.2.4 on 2019-08-25 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaraj_builder', '0005_auto_20190825_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects_completed', models.IntegerField(max_length=10)),
                ('happy_clients', models.IntegerField(max_length=10)),
                ('total_tasks', models.IntegerField(max_length=10)),
                ('entry_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 26, 0, 3, 29, 475578))),
            ],
            options={
                'verbose_name': 'Record',
                'verbose_name_plural': 'Records',
                'db_table': 'record',
                'ordering': ['-entry_date'],
            },
        ),
        migrations.AlterField(
            model_name='quest',
            name='enquiry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 26, 0, 3, 29, 475081)),
        ),
    ]

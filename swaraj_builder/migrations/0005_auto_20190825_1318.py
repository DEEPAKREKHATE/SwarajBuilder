# Generated by Django 2.2.4 on 2019-08-25 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaraj_builder', '0004_auto_20190825_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('enquiry_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 25, 13, 18, 6, 653961))),
            ],
            options={
                'verbose_name': 'Quest',
                'verbose_name_plural': 'Quests',
                'db_table': 'quest',
                'ordering': ['-enquiry_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_date'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='project',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaraj_builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ImageField(upload_to=''),
        ),
    ]

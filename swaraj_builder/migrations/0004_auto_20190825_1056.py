# Generated by Django 2.2.4 on 2019-08-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaraj_builder', '0003_auto_20190825_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='images',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
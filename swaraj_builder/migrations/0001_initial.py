# Generated by Django 2.2.4 on 2019-08-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('images', models.ImageField(upload_to='img/%Y/%m/%d')),
            ],
        ),
    ]

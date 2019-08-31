from django.db import models
from datetime import datetime
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to='%Y/%m/%d')
    created_date = models.DateTimeField(default=datetime.now,blank=True)
    updated_date = models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_date']


class Quest(models.Model):
        first_name = models.CharField(max_length=30)
        phone = models.CharField(max_length=20)
        subject = models.CharField(max_length=50)
        message = models.TextField()
        enquiry_date = models.DateTimeField(default=datetime.now(),blank=True)

        def __str__(self):
            return self.subject

        class Meta:
            db_table = 'quest'
            verbose_name = 'Quest'
            verbose_name_plural = 'Quests'
            ordering = ['-enquiry_date']


class Record(models.Model):
    projects_completed = models.IntegerField()
    happy_clients = models.IntegerField()
    total_tasks = models.IntegerField()
    entry_date = models.DateTimeField(default=datetime.now(),blank=True)

    class Meta:
        db_table = 'record'
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
        ordering = ['-entry_date']






from django.db import models

# Create your models here.
import datetime

class Task(models.Model):
    taskID = models.AutoField(primary_key=True)  # Maps to `int UNSIGNED AUTO_INCREMENT`
    taskCategory = models.CharField(max_length=255)  # Maps to `varchar(255) NOT NULL`
    taskOwner = models.CharField(max_length=255, default="admin")  # Maps to `varchar(255) NOT NULL`
    taskName = models.CharField(max_length=255)  # Maps to `varchar(255) NOT NULL`
    taskDescription = models.TextField()  # Maps to `text(255) NOT NULL`
    taskScheduledFor = models.DateField(default=datetime.date.today)  # Default value is today
    taskCreationDate = models.DateField(auto_now_add=True)  # Maps to `date DEFAULT (CURRENT_DATE)`
    taskStatus = models.IntegerField(default=0)  # Maps to `int DEFAULT 0`

    def __str__(self):
        return f"{self.taskName} by {self.taskOwner} (Scheduled for {self.taskScheduledFor})"




from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key=True)  # Maps to INT UNSIGNED AUTO_INCREMENT    
    username = models.CharField(max_length=255, unique=True)  # Maps to VARCHAR(255), unique
    userPassword = models.CharField(max_length=255)  # Maps to VARCHAR(255)
  

    def __str__(self):
        return self.username
    
    
class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=255, unique=True)
    categoryOwner = models.CharField(max_length=255)  # Change from ForeignKey to CharField

    def __str__(self):
        return self.categoryName



class Task(models.Model):
    taskID = models.AutoField(primary_key=True)  # Maps to INT UNSIGNED AUTO_INCREMENT
    taskName = models.CharField(max_length=255, unique=True)  # Maps to VARCHAR(255), unique
    taskDescription = models.TextField()  # Maps to TEXT, without length restriction
    taskCategory = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='categoryName')  # Foreign Key to `categories` table's `categoryName`
    taskCreationDate = models.DateField(auto_now_add=True)  # Automatically sets current date, Maps to DATE
    taskStatus = models.IntegerField(default=0)  # Maps to INT with default value 0

    def __str__(self):
        return self.taskName


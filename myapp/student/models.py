from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"Data - ID: {self.id}, Name: {self.name}, Email: {self.email}"

class School(models.Model):
    school=models.CharField(max_length=50)
    Standard=models.IntegerField()
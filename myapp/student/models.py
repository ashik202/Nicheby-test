from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"Data - ID: {self.id}, Name: {self.name}, Email: {self.email}"

class School(models.Model):
    student=models.OneToOneField(Student,on_delete=CASCADE,related_name="student")
    school=models.CharField(max_length=50)
    Standard=models.IntegerField()
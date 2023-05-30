from rest_framework import serializers
from .models import Student,School

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id', 'name', 'email']
class SchoolSerializer(serializers.ModelSerializer):
    student=StudentSerializer(read_only=True)
    class Meta:
        model=School
        fields='__all__'
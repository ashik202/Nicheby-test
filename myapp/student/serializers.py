from rest_framework import serializers
from .models import Student,School

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("name","email")
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=("school","Standard")
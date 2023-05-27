
from rest_framework import generics
from .models import Student,School
from .serializers import StudentSerializer,SchoolSerializer
from rest_framework.response import Response
from rest_framework import viewsets

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class SchoolCreateView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer



class CombinedViewSet(viewsets.ViewSet):
    def list(self, request):
        students = Student.objects.all()
        schools = School.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        school_serializer = SchoolSerializer(schools, many=True)
        data = {
            'students': student_serializer.data,
            'schools': school_serializer.data
        }
        return Response(data)
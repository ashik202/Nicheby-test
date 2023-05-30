
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
        queryset = School.objects.select_related('student').all()
        serializer = SchoolSerializer(queryset, many=True)
        return Response(serializer.data)
# urls.py

from django.urls import path,include
from .views import StudentCreateView, SchoolCreateView,CombinedViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r'combined', CombinedViewSet, basename='combined')
urlpatterns = [
    path('student/', StudentCreateView.as_view(), name='student-create'),
    path('school/', SchoolCreateView.as_view(), name='school-create'),
    path('', include(router.urls)),
]

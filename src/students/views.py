from django.shortcuts import render
from django.db.models.query import QuerySet
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student
from .models import Lecturers
from .models import Department
from .models import Course
from .models import Attendence
from .serializers import StudentSerializer
from .serializers import CourseSerializer
from .serializers import LecturersSerializer
from .serializers import AttendenceSerializer
from .serializers import DepartmentSerializer
# Create your views here.

class StudentView(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

class DepartmentView(viewsets.ModelViewSet):
   queryset = Department.objects.all()
   serializer_class = DepartmentSerializer

class CourseView(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class LecturersView(viewsets.ModelViewSet):
   queryset = Lecturers.objects.all()
   serializer_class = LecturersSerializer

class AttendenceView(viewsets.ModelViewSet):
   queryset = Attendence.objects.all()
   serializer_class = AttendenceSerializer
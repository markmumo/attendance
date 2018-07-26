from rest_framework import serializers
from . import models
from .models import Student
from .models import Lecturers
from .models import Department
from .models import Course
from .models import Attendence

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class LecturersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lecturers
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendence
        fields = '__all__'
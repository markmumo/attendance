from rest_framework import serializers
from . import models
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
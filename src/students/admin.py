from django.contrib import admin

# Register your models here.

from .models import Student
from .models import Department
from .models import Course

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)

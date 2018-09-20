from django.contrib import admin

# Register your models here.

from .models import Student
from .models import Department
from .models import Course
from .models import Lecturers
from .models import Attendence

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Lecturers)
admin.site.register(Attendence)
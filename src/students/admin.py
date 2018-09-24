from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

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

class AttendenceResourse(resources.ModelResource):

    class Meta:
        model = Attendence
        fields = ('id', 'registration_number', 'department', 'unit_name', 'start_time', 'end_time', 'date', 'status', 'absent_with_reason', 'detail', )

# class AttendenceAdmin(ImportExportModelAdmin):
#     resource_class = AttendenceResource
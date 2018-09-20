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

# ... export functions will go here ...

class AttendanceAdmin(admin.AttendanceAdmin):
    actions = [export_csv, export_xls, export_xlsx]

admin.site.register(Attendance, AttendanceAdmin)

def export_csv(Attendanceadmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Attendance.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"registration_number"),
        smart_str(u"department"),
        smart_str(u"unit_name"),
        smart_str(u"start_time"),
        smart_str(u"end_time"),
        smart_str(u"date"),
        smart_str(u"status"),
        smart_str(u"absent_with_reason"),
        smart_str(u"detail"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.department),
            smart_str(obj.unit_name),
            smart_str(obj.start_time),
            smart_str(obj.end_time),
            smart_str(obj.date),
            smart_str(obj.status),
            smart_str(obj.absent_with_reason),
            smart_str(obj.detail),
        ])
    return response
export_csv.short_description = u"Export CSV"


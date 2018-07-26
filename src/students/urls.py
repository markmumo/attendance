from django.conf.urls import url, include
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', views.StudentView)
router.register('departments', views.DepartmentView)
router.register('courses', views.CourseView)
router.register('lecturers', views.LecturersView)
router.register('attendences', views.AttendenceView)

urlpatterns = [
    path('', include(router.urls))
]

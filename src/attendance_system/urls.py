"""attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.utils.translation import ugettext_lazy as _
# from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
# from jet.dashboard.dashboard_modules import google_analytics_views
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^students/', include('students.urls')),
    # url(r'^departments/', include('departments.urls')),
    # url(r'^courses/', include('courses.urls')),
    # url(r'^lecturers/', include('lecturers.urls')),
    # url(r'^attendences/', include('attendences.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

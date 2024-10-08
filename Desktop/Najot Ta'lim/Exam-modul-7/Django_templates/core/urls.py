from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('teacher/', include('teacher.urls')),
    path('adminstrator/', include('adminstrator.urls')),
]
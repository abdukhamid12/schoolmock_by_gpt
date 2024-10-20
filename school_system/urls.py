from django.contrib import admin
from django.urls import path, include

from testsystem.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('testsystem.urls')),  # Подключаем API
    path('', home)
]

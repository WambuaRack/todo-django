from django.contrib import admin  # Missing import for admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # Ensure todo/urls.py exists and is correct
]

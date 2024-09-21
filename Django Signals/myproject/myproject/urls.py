from django.contrib import admin
from django.urls import path, include  # Import include to reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('myapp.urls')),   # Include URLs from myapp
]

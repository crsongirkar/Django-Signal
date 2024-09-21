from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    # Example URL patterns
    path('', views.home, name='home'),  # Home page view
    # Add other URL patterns as needed
]

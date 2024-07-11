from django.contrib import admin
from django.urls import path, include
from .views import show_amadeus_settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo.urls')),
    path('show-settings/', show_amadeus_settings),
]


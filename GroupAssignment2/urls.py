from django.urls import path
from main.views import show_main
from django.urls import path, include



urlpatterns = [
    path('', include('main.urls')),
]
from django.urls import path
from main.views import show_main, login, register, adminregister, childregister, caregiverregister, driverregister, userdashboard

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('adminregister/', adminregister, name='adminregister'),
    path('childregister/', childregister, name='childregister'),
    path('caregiverregister/', caregiverregister, name='caregiverregister'),
    path('driverregister/', driverregister, name='driverregister'),
    path('userdashboard/', userdashboard, name="userdashboard")
    
]
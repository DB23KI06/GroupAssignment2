from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
    }

    return render(request, 'main.html', context)

def login(request):
    context = {
    }

    return render(request, 'login.html', context)

def register(request):
    context = {
    }

    return render(request, 'register.html', context)

def adminregister(request):
    context = {
    }

    return render(request, 'adminregister.html', context)

def childregister(request):
    context = {
    }

    return render(request, 'childregister.html', context)

def caregiverregister(request):
    context = {
    }

    return render(request, 'caregiverregister.html', context)

def driverregister(request):
    context = {
    }

    return render(request, 'driverregister.html', context)

def userdashboard(request):
    context = {
    }

    return render(request, 'userdashboard.html', context)
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "profile.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def add(request):
    return render(request, "add-customer.html")


def edit_profile(request):
    return render(request, "edit-profile.html")


def logout(request):
    pass

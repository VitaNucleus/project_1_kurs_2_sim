from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def login_users(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {"user": user}
            return HttpResponseRedirect('/home', headers=context)
    return render(request, 'login.html')


def logout_users(request):
    logout(request)
    return HttpResponseRedirect('/')


def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        check_psswd = request.POST['confirm_password']
        if password == check_psswd:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
    return render(request, 'registration.html')
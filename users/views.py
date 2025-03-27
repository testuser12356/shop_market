from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

import users.form as forms


# Create your views here.
def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    form = forms.RegisterForm()
    return render(request, "auth/register.html", context={"form": form})


def login_user(request):
    if request.POST:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
    form = AuthenticationForm()
    return render(request, "auth/login.html", context={"form": form})


def logout_user(request):
    logout(request)
    return redirect("/")

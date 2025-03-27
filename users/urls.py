from django.urls import path

import users.views as views

urlpatterns = [
    path("login", views.login_user),
    path("register/", views.register),
    path("logout", views.logout_user),
]
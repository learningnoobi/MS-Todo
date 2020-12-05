from django.urls import path
from . import views
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .views import *

urlpatterns = [
    path('register', views.registerPage , name = "register"),
    path('login', views.loginPage , name = "login"),
   ]
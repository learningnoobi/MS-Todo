from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home , name = "home"),
    path('delete/<int:pk>/', views.delete , name = "delete"),
    path('update/<int:pk>/', views.UpdateView , name = "update"),
   ]
   
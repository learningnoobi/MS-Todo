from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home , name = "home"),
    path('delete/<int:pk>/', views.delete , name = "delete"),
    path('update/<int:id>/', views.UpdateView , name = "update"),
    path('detail/<int:pk>/', views.DetailView , name = "detail"),
    path('add/<int:id>/', views.important_post , name = "add"),
    path('important/', views.important_list , name = "important"),

   ]

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home , name = "home"),
    path('delete/<int:pk>/', views.delete , name = "delete"),
    path('update/<int:pk>/', views.UpdateView , name = "update"),
    path('detail/<int:pk>/', DetailView.as_view() , name = "detail"),

   ]
   	# context["side_task"] = Task.objects.filter(author=request.user).order_by("-created")[:3]
	# 	context = super().get_context_data(**kwargs)
	# 	context["side_task"] = Task.objects.filter(author=request.user).order_by("-created")[:3]
	
	# 	return context

""" def get_context_data(self, **kwargs):
	context = super().get_context_data(**kwargs)
	context[""] = 
	return context """
from .models import Task
from django.shortcuts import render,redirect
from.forms import PostForm
from django.contrib.auth.models import User
def context_data(request):

    form = PostForm()
    data = {

        'form':form,
        
        
    }
    return data 
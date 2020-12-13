from django.shortcuts import render,get_object_or_404,redirect
from.models import Task
from django.http import HttpResponseRedirect
from.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

@login_required(login_url='login')
def home(request):
	tasks = Task.objects.filter(author=request.user).order_by("-created")
	side_tasks = Task.objects.filter(author=request.user).order_by("-created")[:3]
	search = request.GET.get('search','')
	if search:
		tasks = tasks.filter(title__icontains=search).order_by("-created")

		
	
	

	if request.method == 'POST':
		form = PostForm(request.POST or None)
		if form.is_valid(): 
              
			obj = form.save(commit = False) 
			obj.author = request.user 
			obj.save() 
			form = PostForm() 
		return redirect('home')
            
	else:
		form = PostForm()
	context = {'tasks':tasks,"form":form,"side_tasks":side_tasks}
	return render(request,'core/home.html',context)


def DetailView(request,pk):
	task = Task.objects.get(id=pk)
	side_tasks = Task.objects.filter(author=request.user).order_by("-created")[:3]
	is_important= False
	if task.important.filter(id=request.user.pk).exists():
		is_important= True

	context={"task":task,'side_tasks':side_tasks,'is_important':is_important}
	return render(request,'core/task_detail.html',context)

def important_post(request,id):
	task = get_object_or_404(Task,id=id)
	if task.important.filter(id=request.user.id).exists():
		task.important.remove(request.user)
	else:
		task.important.add(request.user)
	return HttpResponseRedirect(task.get_absolute_url())

def important_list(request):
	user = request.user
	imp_list = user.important.all()
	context = {
		'imp_list':imp_list
	}
	return render (request,'core/important.html',context)

def UpdateView(request,id):
	instance = get_object_or_404(Task , id=id)
	form = PostForm(instance=instance)
	if request.method == 'POST':
		form = PostForm(request.POST or None,instance=instance)
		if form.is_valid(): 
			form.save()
		return redirect('home')


def delete(request,pk):

	task = Task.objects.get(id=pk)
	
	if request.method=='POST':
		task.delete()
		return redirect('home')
	
from django.shortcuts import render,get_object_or_404,redirect
from.models import Task
from.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as user


@login_required(login_url='login')
def home(request):
	tasks = Task.objects.filter(author=request.user)
	side_tasks = Task.objects.filter(author=request.user)[:3]
	# is_favourite = False
	# if task.important.filter(id=request.user).exists():
	# 	is_favourite = True

	if request.method == 'POST':
		form = PostForm(request.POST or None)
		if form.is_valid(): 
              
			obj = form.save(commit = False) 
			obj.author = request.user 
			obj.save() 
			form = PostForm() 
            
	else:
		form = PostForm()

	context = {'tasks':tasks,"form":form,"side_tasks":side_tasks}
	return render(request,'core/home.html',context)

# def favourite_post(request,id):
# 	task = get_object_or_404(Task,id=id)
# 	if task.important.filter(id=request.user.id).exists():
# 		task.important.remove(request.user)
# 	else:
# 		task.important.add(request.user)
# 	context={}
# 	return render(request,'core/home.html',context)
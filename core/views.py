from django.shortcuts import render
from.models import Task
from.forms import PostForm
def home(request):
	tasks = Task.objects.all().order_by("-created")
	side_tasks = Task.objects.all().order_by("-created")[:3]
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = PostForm

	context = {'tasks':tasks,"form":form,"side_tasks":side_tasks}
	return render(request,'core/home.html',context)
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
	
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)


				return redirect('login')
			

		context = {'form':form}
		return render(request, 'users/register.html', context)

		
		
def loginPage(request):

	if request.user.is_authenticated:
		return redirect('home')

	if request.method =='POST':
		username =request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			messages.warning(request,'Username or password is incorrect')

	context = {}
	return render(request,'users/login.html',context)


def logoutUser(request):
	logout(request)
	return redirect('login')
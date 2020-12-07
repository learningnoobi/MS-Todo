from django import forms
from django.forms import ModelForm
from .models import Task

class PostForm(ModelForm):
	title = forms.CharField(label='', 
               widget=forms.TextInput(
                        attrs={'placeholder': "Add your task", 
                            "class": "form-control"}
                    ))
	class Meta:
		model = Task
		fields =['title','detail']
	


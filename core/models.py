from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	title = models.CharField(max_length=100)
	completed = models.BooleanField(default=False)
	detail = models.TextField(blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	important = models.ManyToManyField(User,related_name="important",blank=True)

	def __str__(self):
		return self.title
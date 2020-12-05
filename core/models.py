from django.db import models

class Task(models.Model):
	title = models.CharField(max_length=100)
	completed = models.BooleanField(default=False)
	detail = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
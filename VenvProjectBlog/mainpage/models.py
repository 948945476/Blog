from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User
@python_2_unicode_compatible
class mainpage(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	create_time = models.DateTimeField()
	author = models.ForeignKey(User) 
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-create_time',]
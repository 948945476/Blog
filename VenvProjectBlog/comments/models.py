#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Comment(models.Model):
	"""docstring for Comment"""
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=255)
	text = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)

	post = models.ForeignKey('blog.Posts')
	
	def __str__(self):
		return self.text[:20]
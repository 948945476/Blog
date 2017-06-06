# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

from django.urls import reverse
@python_2_unicode_compatible
class Category(models.Model):
	'''文章类别类'''
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Tag(models.Model):
	'''文章标签类'''
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Posts(models.Model):
	'''文章内容类'''
	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	#创建时间
	modified_time = models.DateTimeField()
	#修改时间
	excerpt = models.CharField(max_length=200, blank=True)
	#摘要
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User)
	showNum = models.BigIntegerField(default=0)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-created_time', 'title']
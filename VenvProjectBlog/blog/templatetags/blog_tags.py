#-*- coding:utf-8 -*-
from ..models import Posts, Category
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
	return Posts.objects.all()[:num]

@register.simple_tag
def archives():
	return Posts.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
	category_list = Category.objects.annotate(num_post=Count('posts'))
	return category_list
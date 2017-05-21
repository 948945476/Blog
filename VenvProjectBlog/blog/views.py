# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Posts, Category
from django.shortcuts import get_object_or_404
from comments.forms import CommentForm
import markdown



def  index(request):
	# return HttpResponse('欢迎访问我的主页')
	post_list = Posts.objects.all()
	return render(request, 'blog/index.html',context={
			'title':'我的博客首页',
			'welcome':'欢迎访问我的博客主页',
			'post_list':post_list
		})

def detail(request, pk):
	post = get_object_or_404(Posts, pk=pk)
	post.body = markdown.markdown(post.body, extensions=[
		'markdown.extensions.extra', 
		'markdown.extensions.codehilite', 
		'markdown.extensions.toc'])

	form = CommentForm()
	comment_list = post.comment_set.all()
	context = {
	'post':post,
	'form':form,
	'comment_list':comment_list,
	}

	return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
	post_list = Posts.objects.filter(created_time__year=year, created_time__month=month)
	return render(request, 'blog/index.html', context={'post_list':post_list})

def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	post_list = Posts.objects.filter(category=cate)
	return render(request, 'blog/index.html', context={'post_list':post_list})

def search(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = "输入搜索数据为空"
		return render(request, 'blog/index.html', context={'error_msg':error_msg})

	post_list = Posts.objects.filter(title__icontains=q)
	if len(post_list) == 0:
		context = {
		'error_msg':"查询失败，该条件下没有查询结果",
		'text_css':"danger",
		'post_list':post_list,
		}
	else:
		context = {
		'error_msg':"查询成功，该条件下查询结果如下",
		'text_css':"success",
		'post_list':post_list,
		}
	return render(request, 'blog/index.html', context=context)


# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from .models import mainpage,about
import markdown

def pagetxt(request):
	main = get_object_or_404(mainpage,pk=1)
	main.body = markdown.markdown(main.body, extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.codehilite',
		'markdown.extensions.toc'])
	return render(request, 'blog/main.html', context={'main':main})

def pageabout(request):
	main =get_object_or_404(about)
	main.pictxt = markdown.markdown(main.pictxt, extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.codehilite',
		'markdown.extensions.toc'])
	main.about = markdown.markdown(main.about, extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.codehilite',
		'markdown.extensions.toc'])
	return render(request, 'blog/about.html', context={'main':main})
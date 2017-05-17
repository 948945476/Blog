#-*- coding:utf-8 -*-
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'text']

		widgets = {
		'name':forms.TextInput(attrs={'placeholder':'名字',}),
		'email':forms.TextInput(attrs={'placeholder':'邮箱',}),
		}
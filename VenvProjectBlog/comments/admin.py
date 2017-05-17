from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
	list_display = ['pk','post']
admin.site.register(Comment,CommentAdmin)
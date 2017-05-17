from django.contrib import admin

# Register your models here.
from .models import Posts,Category,Tag

class PostAdmin(admin.ModelAdmin):
	list_display = ['pk', 'title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Posts, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
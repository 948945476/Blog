from django.contrib import admin

# Register your models here.
from .models import mainpage,about
admin.site.register(mainpage)
admin.site.register(about)
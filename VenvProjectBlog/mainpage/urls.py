from django.conf.urls import url
from . import views

app_name="mainpage"
urlpatterns=[
	url(r"^[index]?$", views.pagetxt, name='pagetxt'),
	url(r'^about', views.pageabout, name='pageabout'),
]
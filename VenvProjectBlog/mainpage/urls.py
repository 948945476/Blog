from django.conf.urls import url
from . import views

app_name="mainpage"
urlpatterns=[
	url(r'^$', views.pagetxt, name='pagetxt'),
]
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	path(r'ke/', views.ke),
	path(r'AAA1/', views.AAA1),
]
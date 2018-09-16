from . import views
from django.urls import path
app_name = 'instamojo'
urlpatterns = [
	path('', views.index ,name = 'index'),
	
]
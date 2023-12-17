from django.urls import path, include
from . import views


app_name = 'learning'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('exercises', views.exercises, name='exercises'),
]

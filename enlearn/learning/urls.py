from django.urls import path, include
from . import views


app_name = 'learning'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('exercises', views.exercises, name='exercises'),
    path('exercises/remember', views.remember_all, name='remember_all'),
    path('exercises/biathlon', views.biathlon, name='biathlon'),
    path('',views.get_all_studywords, name='get_all_studywords')
]

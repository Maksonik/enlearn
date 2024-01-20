from django.urls import path, include
from . import views
from .views import register

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('', views.view_base, name='dashboard'),
    path('change-level-word/', views.change_level_word, name='change_level_word'),
    path('create_study_word/', views.create_study_word, name='create_study_word'),
    path('check_study_word/', views.check_study_word, name='check_study_word'),
]

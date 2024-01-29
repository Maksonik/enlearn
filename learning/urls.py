from django.urls import path
from . import views

app_name = 'learning'

urlpatterns = [
    path('', views.all_study_words, name='get_all_studywords'),
    path('profile', views.profile, name='profile'),
    path('exercises', views.exercises, name='exercises'),
    path('exercises/remember', views.remember_all, name='remember_all'),
    path('exercises/biathlon', views.biathlon, name='biathlon'),
    path('change-level-word/', views.change_level_word, name='change_level_word'),
    path('create_study_word/', views.create_study_word, name='create_study_word'),
    path('is_study_word/', views.is_study_word, name='is_study_word'),
]

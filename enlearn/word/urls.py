from django.urls import path
from .views import word_detail

app_name = 'words'

urlpatterns = [
    path('', word_detail, name='word_detail'),
]

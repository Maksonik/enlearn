from django.urls import path, include
from .views import word_detail

urlpatterns = [
    path('<str:name>/', word_detail, name='word_detail'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:title>', views.WordDetail, name='detail_word'),
]


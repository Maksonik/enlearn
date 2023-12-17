from django.urls import path
from .views import word_detail, word_list

app_name = 'words'

urlpatterns = [
    path('', word_detail, name='word_detail'),
    path('list/', word_list, name='word_list')
]

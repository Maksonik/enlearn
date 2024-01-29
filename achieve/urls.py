from django.urls import path
from . import views

app_name = 'achieve'

urlpatterns = [
    path('achieve-list/', views.list_achieve, name='list_achieve')
]

from django.urls import path, include
from . import views
from .views import register

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('', views.view_base, name='dashboard'),
]

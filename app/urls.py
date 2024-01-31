from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.random_sushi, name='random_sushi'),
]

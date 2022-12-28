from django.contrib import admin
from django.urls import path

from base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dictionary', views.manage_dictionary.as_view(), name='manage_dictionary')
]

from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', home),
    path('api/get-hotels/', get_hotel),  
]
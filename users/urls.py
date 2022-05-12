
from django.contrib import admin
from django.urls import path
from .views import loginUser, index

urlpatterns = [
    path('', index, name='index'),
    path('login/', loginUser, name='login'),
]

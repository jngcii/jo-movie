from django.urls import path
from . import views

app_name = 'movies'

ulrpatterns = [
    path('', views.search, name='search'),
]
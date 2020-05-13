from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.search, name='search'),
    path('scrap/', views.scrap, name='scrap'),
]
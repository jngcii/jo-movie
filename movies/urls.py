from django.urls import path

app_name = 'movies'

ulrpatterns = [
    path('', views.index, name='index')
]
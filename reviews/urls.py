from django.urls import path
from . import views

app_name = 'reviews'

ulrpatterns = [
    path('<int:review_pk>/', views.detail, name='detail'),
    path('create/<int:movie_pk>/', views.create_review, name='create_review'),
    path('update/<int:review_pk>/', views.update_review, name='update_review'),
    path('delete/<int:review_pk>/', views.delete_review, name='delete_review'),
]